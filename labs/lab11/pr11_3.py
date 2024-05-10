# Упражнение 11.3

import numpy as np
from thinkdsp import Wave
from thinkdsp import read_wave


def sample(wave, factor):
    """Simulates sampling of a wave."""

    ys = np.zeros(len(wave))
    ys[::factor] = np.real(wave.ys[::factor])
    return Wave(ys, framerate=wave.framerate)


wave = read_wave('../../code/263868__kevcio__amen-break-a-160-bpm.wav')
wave.normalize()
wave.plot()
wave.make_audio()

spectrum = wave.make_spectrum(full=True)
spectrum.plot()

factor = 3
framerate = wave.framerate / factor
cutoff = framerate / 2 - 1

spectrum.low_pass(cutoff)
spectrum.plot()

filtered = spectrum.make_wave()
filtered.make_audio()

sampled = sample(filtered, factor)
sampled.make_audio()

sampled_spectrum = sampled.make_spectrum(full=True)
sampled_spectrum.plot()

sampled_spectrum.low_pass(cutoff)
sampled_spectrum.plot()

sampled_spectrum.scale(factor)
spectrum.plot()
sampled_spectrum.plot()

print(spectrum.max_diff(sampled_spectrum))

interpolated = sampled_spectrum.make_wave()
interpolated.make_audio()

filtered.plot()
interpolated.plot()

print(filtered.max_diff(interpolated))
