import aspectlib


class Config:
    sampling_rate = 44100
    duration = 2
    hop_length = 347 * duration  # to make time steps 128
    f_min = 20
    f_max = sampling_rate // 2
    n_images = 128
    n_fft = n_images * 20
    samples = sampling_rate * duration


@aspectlib.Aspect
def init(*args, **kwargs):
    print("Initializing new Audio Expert ...")
    if 'config' not in kwargs:
        print('Config was none, inserting default config')
        kwargs.update({"config": Config()})
        yield aspectlib.Proceed(*args, **kwargs)
    else:
        print('Config is present, passing it further')
        yield aspectlib.Proceed
    print("Successfully initialized audio expert")
