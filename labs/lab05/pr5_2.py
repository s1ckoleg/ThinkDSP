# Упражнение 5.2

from matplotlib import pyplot as plt
from autocorr import autocorr
import numpy as np
from thinkdsp import read_wave, decorate


def estimate_fundamental(segment, low=70, high=150):
    lags, corrs = autocorr(segment)
    lag = np.array(corrs[low:high]).argmax() + low
    period = lag / segment.framerate
    frequency = 1 / period
    return frequency


wave = read_wave('../../code/28042__bcjordan__voicedownbew.wav')
wave.normalize()
wave.make_audio()

wave.make_spectrogram(2048).plot(high=4200)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')

duration = 0.01
segment = wave.segment(start=0.2, duration=duration)
freq = estimate_fundamental(segment)
print(freq)

step = 0.05
starts = np.arange(0.0, 1.4, step)

ts = []
freqs = []

for start in starts:
    ts.append(start + step/2)
    segment = wave.segment(start=start, duration=duration)
    freq = estimate_fundamental(segment)
    freqs.append(freq)

wave.make_spectrogram(2048).plot(high=900)
plt.plot(ts, freqs, color='white')
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
