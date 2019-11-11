import librosa
import numpy as np
import librosa.display
import matplotlib.pyplot as plt
from dev.clink.aspects.experts.audio_expert import init


class AudioExpert:
    @init
    def __init__(self, config=None):
        self.config = config

    def read_audio(self, pathname, trim_long_data):
        y, sr = librosa.load(pathname, sr=self.config.sampling_rate)

        # trim silence
        if 0 < len(y):  # workaround: 0 length causes error
            y, _ = librosa.effects.trim(y)  # trim, top_db=default(60)

        # make it unified length to conf.samples
        if len(y) > self.config.samples:  # long enough
            if trim_long_data:
                y = y[0:0 + self.config.samples]
        else:  # pad blank
            padding = self.config.samples - len(y)  # add padding at both ends
            offset = padding // 2
            y = np.pad(y, (offset, self.config.samples - len(y) - offset), 'constant')
        return y

    def audio_to_melspectrogram(self, audio):
        spectrogram = librosa.feature \
            .melspectrogram(audio,
                            sr=self.config.sampling_rate,
                            n_mels=self.config.n_images,
                            hop_length=self.config.hop_length,
                            n_fft=self.config.n_fft,
                            fmin=self.config.f_min,
                            fmax=self.config.f_max)
        spectrogram = librosa.power_to_db(spectrogram)
        spectrogram = spectrogram.astype(np.float32)
        return spectrogram

    def read_as_melspectrogram(self, pathname, trim_long_data):
        x = self.read_audio(pathname, trim_long_data)
        mels = self.audio_to_melspectrogram(x)
        return mels

    def show_melspectrogram(self, spectrogram, title='Log-frequency power spectrogram'):
        librosa.display \
            .specshow(spectrogram, x_axis='time', y_axis='mel',
                      sr=self.config.sampling_rate, hop_length=self.config.hop_length,
                      fmin=self.config.f_min, fmax=self.config.f_max)
        plt.colorbar(format='%+2.0f dB')
        plt.title(title)
        plt.show()
