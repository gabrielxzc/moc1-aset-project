import pickle
import dev.clink.aspects.experts.storage_expert as aspects


# @aspects.save_object_aspect
def save_object(path, obj):
    with open(path, "wb") as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)


# @aspects.load_aspect
def load(path):
    with open(path, "rb") as handle:
        return pickle.load(handle)
