from dev.clink.converters.converter import Converter
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack
import numpy as np
from matplotlib import pyplot as plt


class FftConverter(Converter):
    def convert_wav(self, sound_path):
        frequency, signal = wavfile.read(sound_path)
        l_audio = len(signal.shape)
        if l_audio == 2:
            signal = signal.sum(axis=1) / 2
        n = signal.shape[0]
        secs = n / float(frequency)
        Ts = 1.0 / frequency
        t = scipy.arange(0, secs, Ts)
        fft = abs(scipy.fft(signal))
        fft_side = abs(fft[range(n // 2)])
        frequencies = scipy.fftpack.fftfreq(signal.size, t[1] - t[0])
        frequencies_side = frequencies[range(n // 2)]  # one side frequency range
        # use frequencies_side and ff_side
        m = fft_side.mean()
        sd = fft_side.std()
        fft_side = (fft_side - m) / sd
        m = frequencies_side.mean()
        sd = frequencies_side.std()
        frequencies_side = (frequencies_side - m) / sd
        return np.hstack(
            (
                np.array([fft_side, frequencies_side]).T,
                np.expand_dims(np.zeros(len(fft_side)), axis=1),
            )
        )

    def get_destination_root(self):
        return "../data/fft"
