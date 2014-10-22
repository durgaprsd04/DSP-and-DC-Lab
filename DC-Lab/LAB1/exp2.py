import numpy as np
import pylab as py
fs = 10000000
fc = 1000
t = np.arange(0.1,.001,1/fs)
tmax = .001
dt = .001/fc
t1 = np.arange(0,tmax,dt)
x = np.sin(2 * pi * fs * t)
data = np.random.randint(0,2,1024)
y = []
x=test
