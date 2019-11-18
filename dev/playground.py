import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack
import numpy as np
from matplotlib import pyplot as plt


def fft_example(path):
    frequency, signal = wavfile.read(path)
    print(f'Frequency: {frequency}')
    l_audio = len(signal.shape)
    print("Channels", l_audio)
    if l_audio == 2:
        signal = signal.sum(axis=1) / 2
    n = signal.shape[0]
    print("Complete Samplings n", n)
    secs = n / float(frequency)
    print("secs", secs)
    Ts = 1.0 / frequency  # sampling interval in time
    print("Timestep between samples Ts", Ts)
    t = scipy.arange(0, secs, Ts)  # time vector as scipy arange field / numpy.ndarray
    FFT = abs(scipy.fft(signal))
    FFT_side = FFT[range(n // 2)]  # one side FFT range
    freqs = scipy.fftpack.fftfreq(signal.size, t[1] - t[0])
    fft_freqs = np.array(freqs)
    freqs_side = freqs[range(n // 2)]  # one side frequency range
    fft_freqs_side = np.array(freqs_side)
    plt.subplot(311)
    p1 = plt.plot(t, signal, "g")  # plotting the signal
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.subplot(312)
    p2 = plt.plot(freqs, FFT, "r")  # plotting the complete fft spectrum
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Count dbl-sided')
    plt.subplot(313)
    p3 = plt.plot(freqs_side, abs(FFT_side), "b")  # plotting the positive fft spectrum
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Count single-sided')
    plt.show()


if __name__ == '__main__':
    # wav_fft_playground()
    path1 = '../data/sounds/train_curated/0a9bebde.wav'
    path2 = '../data/sounds/train_curated/0a9c90be.wav'
    fft_example(path1)
    fft_example(path2)
