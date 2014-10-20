import numpy as np
import pylab as py
f = 2000
fs1 = 3000
fs2 = 5000
fs3 = 15000
# Making a waveform of length 4T
t = np.arange(0,4.0/f,1.0/(1000*f))
xa = np.sin(2 * np.pi * f * t)
print len(xa)
sample_points = ((1.0 * f)/fs1 )*1000
sampled = np.sin(2 * np.pi * f * t*0)
init = sample_points
while sample_points < len(sampled):
    sampled[sample_points] = xa[sample_points]
    sample_points = sample_points+ init
sampled1 = np.sin(2 * np.pi *f * t * 0)
print len(sampled1)
sample_points1 = ((1.0 * f)/fs2)*1000
init = sample_points1
while sample_points1< len(sampled1):
    sampled1[sample_points1] = xa[sample_points1]
    sample_points1 = sample_points1+ init
    print sample_points1
# Putting in subplots
py.subplot(3, 1, 1)
py.plot(t, xa)
py.subplot(3, 1, 2)
py.stem(t, sampled,'-')
py.subplot(3, 1, 3)
py.stem(t, sampled1,'-')
py.ylabel('Amplitude(Normalized)',size='medium')
py.xlabel('Time(in ms)',size='medium')
py.savefig('ouputdifferent.png',dpi=(300))
py.close()
# Putting in a single graph
py.plot(t, xa,t, sampled,t,sampled1)
py.title('Sampled waveforms')
py.legend(['Waveform','3KHz Sampling','5KHz Sampling'])
py.xlabel("Time(ms)")
py.ylabel("Amplitude(normalized)")
py.savefig('outputcombined.png',dpi=(300))
py.close()
# Sampling in 15KHz
sample_points2 = ((1.0 * f)/fs3 )*1000
sampled2 = np.sin(2 * np.pi * f * t*0)
init = sample_points2
while sample_points2 < len(sampled):
    sampled2[sample_points2] = xa[sample_points2]
    sample_points2 = sample_points2+ init
# Putting in Quantization

