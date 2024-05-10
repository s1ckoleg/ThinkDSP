# Упражнение 6.1

from thinkdsp import UncorrelatedGaussianNoise
from scipy.stats import linregress
import scipy.fftpack
import numpy as np
from matplotlib import pyplot as plt
from thinkdsp import decorate
import timeit


def func(ys, freqs, ts):
    pass


def scipy_dct(ys, freqs, ts):
    return scipy.fftpack.dct(ys, type=3)


def analyze1(ys, fs, ts):
    """Analyze a mixture of cosines and return amplitudes."""
    args = np.outer(ts, fs)
    M = np.cos(PI2 * args)
    amps = np.linalg.solve(M, ys)
    return amps


def analyze2(ys, fs, ts):
    """Analyze a mixture of cosines and return amplitudes."""
    args = np.outer(ts, fs)
    M = np.cos(PI2 * args)
    amps = np.dot(M, ys) / 2
    return amps


def plot_bests(ns, bests):
    plt.plot(ns, bests)
    decorate(**loglog)

    x = np.log(ns)
    y = np.log(bests)
    t = linregress(x, y)
    slope = t[0]

    return slope


def run_speed_test(ns, func):
    stmt = "func(ys, freqs, ts)"
    setup = "from pr6_1 import func, ys, freqs, ts"
    results = []
    for N in ns:
        print(N)
        ts = (0.5 + np.arange(N)) / N
        freqs = (0.5 + np.arange(N)) / 2
        ys = noise.ys[:N]
        result = timeit.timeit(stmt, setup=setup, number=1)
        results.append(result)

    bests = [result.best for result in results]
    return bests


signal = UncorrelatedGaussianNoise()
noise = signal.make_wave(duration=1.0, framerate=16384)
print(noise.ys.shape)

loglog = dict(xscale='log', yscale='log')
PI2 = np.pi * 2

ns = 2 ** np.arange(6, 13)
print(ns)

bests = run_speed_test(ns, analyze1)
plot_bests(ns, bests)

bests2 = run_speed_test(ns, analyze2)
plot_bests(ns, bests2)

bests3 = run_speed_test(ns, scipy_dct)
plot_bests(ns, bests3)

plt.plot(ns, bests, label='analyze1')
plt.plot(ns, bests2, label='analyze2')
plt.plot(ns, bests3, label='fftpack.dct')
decorate(xlabel='Wave length (N)', ylabel='Time (s)', **loglog)
