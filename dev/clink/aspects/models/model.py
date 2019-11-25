import subprocess
from typing import Generator

import aspectlib
import keras


def get_gpu_memory_map() -> dict:
    """Get the current gpu usage.

    Returns
    -------
    usage: dict
        Keys are device ids as integers.
        Values are memory usage as integers in MB.
    """
    result = subprocess.check_output(
        ["nvidia-smi", "--query-gpu=memory.total", "--format=csv,nounits,noheader"]
    )
    result = result.decode("utf-8")
    # Convert lines into a dictionary
    gpu_memory = [int(x) for x in result.strip().split("\n")]
    gpu_memory_map = dict(zip(range(len(gpu_memory)), gpu_memory))
    return gpu_memory_map


def get_model_memory_usage(model: keras.Model) -> float:
    """
    Return the total amount of memory that will be used by the model based on its architecture
    :param model: keras model
    :return: memory in mb
    """
    import numpy as np
    from keras import backend as K

    shapes_mem_count = 0
    internal_model_mem_count = 0
    for l in model.layers:
        layer_type = l.__class__.__name__
        if layer_type == "Model":
            internal_model_mem_count += get_model_memory_usage(l)
        single_layer_mem = 1
        for s in l.output_shape:
            if s is None:
                continue
            single_layer_mem *= s
        shapes_mem_count += single_layer_mem

    trainable_count = np.sum([K.count_params(p) for p in set(model.trainable_weights)])
    non_trainable_count = np.sum(
        [K.count_params(p) for p in set(model.non_trainable_weights)]
    )

    number_size = 4.0
    if K.floatx() == "float16":
        number_size = 2.0
    if K.floatx() == "float64":
        number_size = 8.0

    total_memory = number_size * (
        shapes_mem_count + trainable_count + non_trainable_count
    )
    gbytes = np.round(total_memory / (1024.0 ** 3), 3) + internal_model_mem_count
    return gbytes * 1024


@aspectlib.Aspect
def fit(*args, **kwargs) -> Generator:
    # TODO: take in account the number of GPUs

    print(kwargs)
    total_memory = get_gpu_memory_map()[0]
    print("total GPU memory", total_memory)

    learner = args[0]
    memory_per_single_instance = get_model_memory_usage(learner.model)
    print("memory per model instance", memory_per_single_instance)

    recommended_batch_size = total_memory // memory_per_single_instance
    if recommended_batch_size > 128:
        recommended_batch_size = 128

    kwargs.update({"batch_size": int(recommended_batch_size)})
    print("Using recommended batch size", recommended_batch_size)
    yield aspectlib.Proceed(*args, **kwargs)
