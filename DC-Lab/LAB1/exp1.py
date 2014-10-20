import numpy as np
import pylab as py
f = 2
t = np.arange(0,10/f, .001/f)
x = np.sin(2* np.pi * f * t)
xa = np.sin(2*np.pi * f*t * 0)
for i in range(0,len(x)):
    if i < len(x)/5:
        xa[i] = 1
    elif i > len(x)/5 and i < 2*len(x)/5:
        xa[i]=-1
    elif i > 2*len(x)/5 and i < (3*len(x))/5:
        xa[i]=1
    elif i > 3*len(x)/5 and i < (4*len(x))/5:
        xa[i]=-1
    else:
        xa[i] =1

py.plot(t,xa)
py.show()
py.close()
py.plot(t,xa)
py.show()
py.close()
bpsk = np.sin(2 * np.pi * f * t * 0)
for i in range(0,len(x)):
    bpsk[i] = xa[i]*x[i]
py.plot(t,bpsk)
py.show()
py.close()

