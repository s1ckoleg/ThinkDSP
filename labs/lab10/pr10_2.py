# Упражнение 10.2

from thinkdsp import read_wave, decorate

response = read_wave('../../code/stalbans_a_mono.wav')

start = 0
duration = 5
response = response.segment(duration=duration)
response.shift(-start)

response.normalize()
response.plot()
decorate(xlabel='Time (s)')

response.make_audio()

transfer = response.make_spectrum()
transfer.plot()
decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')

transfer.plot()
decorate(xlabel='Frequency (Hz)', ylabel='Amplitude', xscale='log', yscale='log')

wave = read_wave('../../code/170255__dublie__trumpet.wav')

start = 0.0
wave = wave.segment(start=start)
wave.shift(-start)

wave.truncate(len(response))
wave.normalize()
wave.plot()
decorate(xlabel='Time (s)')
wave.make_audio()

spectrum = wave.make_spectrum()
print(len(spectrum.hs), len(transfer.hs))
print(spectrum.fs)
print(transfer.fs)

output = (spectrum * transfer).make_wave()
output.normalize()

wave.plot()
output.plot()
output.make_audio()

convolved2 = wave.convolve(response)
convolved2.normalize()
convolved2.make_audio()
