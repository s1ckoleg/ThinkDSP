# Упражнение 6.2

import numpy as np
from thinkdsp import Spectrogram
from thinkdsp import read_wave, decorate


def make_dct_spectrogram(wave, seg_length):
    """Computes the DCT spectrogram of the wave."""
    window = np.hamming(seg_length)
    i, j = 0, seg_length
    step = seg_length // 2
    spec_map = {}

    while j < len(wave.ys):
        segment = wave.slice(i, j)
        segment.window(window)

        t = (segment.start + segment.end) / 2
        spec_map[t] = segment.make_dct()

        i += step
        j += step

    return Spectrogram(spec_map, seg_length)


def compress(dct, thresh=1):
    count = 0
    for i, amp in enumerate(dct.amps):
        if np.abs(amp) < thresh:
            dct.hs[i] = 0
            count += 1

    n = len(dct.amps)
    print(count, n, 100 * count / n, sep='\t')


wave = read_wave('../../code/100475__iluppai__saxophone-weep.wav')
wave.make_audio()

segment = wave.segment(start=1.2, duration=0.5)
segment.normalize()
segment.make_audio()

seg_dct = segment.make_dct()
seg_dct.plot(high=4000)
decorate(xlabel='Frequency (Hz)', ylabel='DCT')

seg_dct = segment.make_dct()
compress(seg_dct, thresh=10)
seg_dct.plot(high=4000)

seg2 = seg_dct.make_wave()
seg2.make_audio()

spectro = make_dct_spectrogram(wave, seg_length=1024)
for t, dct in sorted(spectro.spec_map.items()):
    compress(dct, thresh=0.2)

wave2 = spectro.make_wave()
wave2.make_audio()
