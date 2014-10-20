import numpy as np
import pylab as py
f1 = 1./8
f2 = 7./8
fs = 1
t = np.arange(0, 1.0/f1, 1.0/(1000*f1))
xa1 = np.sin(2 * np.pi * f1 * t)
xa2 = np.sin(2 * np.pi * f2 * t)
# Now we have to sample
# Having some points where we could put the value
# Sampling Signal one
# fs=10
xsa1 = np.sin(2*np.pi*f1*t*0)
sampled_points = ((1.0 * f1)/fs)*1000
init = sampled_points
while sampled_points < len(xsa1):
    xsa1[sampled_points] = xa1[sampled_points]
    sampled_points = sampled_points + init
# Sampling signal two
# fs = 10
xsa2 = np.sin(2 * np.pi * f2 * t * 0)
sampled_points = ((1.0 * f1)/fs)*1000
init = sampled_points
while sampled_points < len(xsa2):
    xsa2[sampled_points] = xa2[sampled_points]
    sampled_points = sampled_points + init
print len(t)
# Plotting the first set sampling frequency
py.subplot(2, 1, 1)
py.plot(t, xa1)
py.stem(t, xsa1, '-r')
py.subplot(2, 1, 2)
py.plot(t, xa2)
py.stem(t, xsa2, '-g')
py.savefig('sampled1.png')
py.close()
# Plotting at a higher frequency
fs = 7/2
# fs = 2
xsa1 = np.sin(2*np.pi*f1*t*0)
sampled_points = ((1.0 * f1)/fs)*1000
init = sampled_points
while sampled_points < len(xsa1):
    xsa1[sampled_points] = xa1[sampled_points]
    sampled_points = sampled_points + init
# Sampling signal two
# fs = 10
xsa2 = np.sin(2 * np.pi * f2 * t * 0)
sampled_points = ((1.0 * f1)/fs)*1000
init = sampled_points
while sampled_points < len(xsa2):
    xsa2[sampled_points] = xa2[sampled_points]
    sampled_points = sampled_points + init
print len(t)
# Plotting the first set sampling frequency
py.subplot(2, 1, 1)
py.plot(t, xa1)
py.stem(t, xsa1, '-r')
py.subplot(2, 1, 2)
py.plot(t, xa2)
py.stem(t, xsa2, '-g')
py.savefig('sampled2.png')
py.close()
# Second Part
xn = [1, 1, 1, 0, 1, 2, 3, 4]
t1 = np.arange(0, 8)
py.stem(t1, xn)
py.savefig('signal1.png')
py.close()
xn1 = np.array([])
for i, item in enumerate(reversed(xn)):
    xn1 = np.append(xn1, item)
t2 = np.arange(-7, 1)
py.stem(t2, xn1)
py.savefig('signal2.png')
py.close()
t3 = np.arange(-5, 3)
py.stem(t3, xn1)
py.savefig('signal3.png')
py.close()
# Convolution
# We have got an h[n] . So mostly we will be using it directly
hn = np.array([1, 2, 1, -1])
conv = []
conv = np.convolve(xn, hn)
py.subplot(221)
py.ylabel("Amplitude")
py.title("x[n]")
py.stem(t1, xn)
py.subplot(222)
py.ylabel("Amplitude")
py.title("h[n]")
py.stem(hn)
t2 = np.arange(-3, 1)
hn1 = np.array([])
for i, item in enumerate(reversed(hn)):
    hn1 = np.append(hn1, item)
py.subplot(223)
py.xlabel("time")
py.ylabel("Amplitude")
py.title("h[-n]")
py.stem(t2, hn1)
py.subplot(224)
py.xlabel("time")
py.ylabel("Amplitude")
py.ALLOW_THREADS
py.title("Convolution Output")
py.stem(conv)
py.savefig('signal4.png')
py.close()
print conv
# Stability of the signal
a = .9
p = np.arange(0, 21, 1)
sig = np.power(a, p)
py.subplot(221)
py.stem(p, sig)
py.title("0<a<1, p > 1")
p = np.arange(-20, 0, 1)
sig = np.power(a, p)
py.subplot(222)
py.stem(p, sig)
py.title("a < 1, p < 0")
a = -0.9
p = np.arange(0, 21, 1)
sig = np.power(a, p)
py.subplot(223)
py.stem(p, sig)
py.title("-1<a<0, p>0")
p = range(-20, 0, 1)
sig = np.power(a, p)
py.subplot(224)
py.stem(p, sig)
py.title('-1<a<0, p < 0')
py.savefig("stability.png")
py.close()
