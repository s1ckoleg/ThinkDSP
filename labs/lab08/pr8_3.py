# Упражнение 8.3

from matplotlib import pyplot as plt
import scipy
import numpy as np
from thinkdsp import SquareSignal
from thinkdsp import decorate


def zero_pad(array, n):
    """Extends an array with zeros."""

    res = np.zeros(n)
    res[:len(array)] = array
    return res


def plot_window_dfts(windows, names):
    for window, name in zip(windows, names):
        padded =  zero_pad(window, len(wave))
        dft_window = np.fft.rfft(padded)
        plt.plot(abs(dft_window), label=name)


signal = SquareSignal(freq=440)
wave = signal.make_wave(duration=1.0, framerate=44100)

M = 15
std = 2.5

gaussian = scipy.signal.gaussian(M=M, std=std)
bartlett = np.bartlett(M)
blackman = np.blackman(M)
hamming = np.hamming(M)
hanning = np.hanning(M)

windows = [blackman, gaussian, hanning, hamming]
names = ['blackman', 'gaussian', 'hanning', 'hamming']

for window in windows:
    window /= sum(window)

for window, name in zip(windows, names):
    plt.plot(window, label=name)

decorate(xlabel='Index')

plot_window_dfts(windows, names)
decorate(xlabel='Frequency (Hz)')

plot_window_dfts(windows, names)
decorate(xlabel='Frequency (Hz)', yscale='log')
