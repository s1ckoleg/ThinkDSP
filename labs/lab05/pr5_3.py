# Упражнение 5.3

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from thinkdsp import Wave
from thinkdsp import decorate
from autocorr import autocorr

df = pd.read_csv(
    filepath_or_buffer='../../code/BTC_USD_2013-10-01_2020-03-26-CoinDesk.csv',
    parse_dates=[0]
)

ys = df['Closing Price (USD)']
ts = df.index

wave = Wave(ys, ts, framerate=1)
wave.plot()
decorate(xlabel='Time (days)', ylabel='Price of BitCoin ($)')

lags, corrs = autocorr(wave)
plt.plot(lags, corrs)
decorate(xlabel='Lag', ylabel='Correlation')

N = len(wave)
corrs2 = np.correlate(wave.ys, wave.ys, mode='same')
lags = np.arange(-N//2, N//2)
plt.plot(lags, corrs2)
decorate(xlabel='Lag', ylabel='Dot product')

N = len(corrs2)
half = corrs2[N//2:]
plt.plot(half)
decorate(xlabel='Lag', ylabel='Dot product')

lengths = range(N, N//2, -1)
half /= lengths
half /= half[0]
plt.plot(half)
decorate(xlabel='Lag', ylabel='Dot product')

plt.plot(corrs, label='autocorr')
plt.plot(half, label='correlate')
decorate(xlabel='Lag', ylabel='Correlation')
