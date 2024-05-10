# Упражнение 10.1

import scipy.signal
from thinkdsp import Wave
from thinkdsp import decorate, read_wave

response = read_wave('../../code/180960__kleeb__gunshot.wav')

start = 0.12
response = response.segment(start=start)
response.shift(-start)

response.truncate(2**16)
response.zero_pad(2**17)

response.normalize()
response.plot()
decorate(xlabel='Time (s)')

transfer = response.make_spectrum()
transfer.plot()
decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')

violin = read_wave('../../code/92002__jcveliz__violin-origional.wav')

start = 0.11
violin = violin.segment(start=start)
violin.shift(-start)

violin.truncate(2**16)
violin.zero_pad(2**17)

violin.normalize()
violin.plot()
decorate(xlabel='Time (s)')

spectrum = violin.make_spectrum()

output = (spectrum * transfer).make_wave()
output.normalize()
output.plot()
output.make_audio()

response.truncate(2**16)
response.plot()

violin.truncate(2**16)
violin.plot()

output2 = violin.convolve(response)
output2.plot()
output2.make_audio()

print(len(output), len(output2))

ys = scipy.signal.fftconvolve(violin.ys, response.ys)
output3 = Wave(ys, framerate=violin.framerate)
output3.plot()
output3.make_audio()

print(output2.max_diff(output3))
