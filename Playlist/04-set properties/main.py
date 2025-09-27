import matplotlib.pyplot as plt
import numpy as np

# membuat data
def sinusGenerator(amplitudo,frekuensi,waktuAkhir,theta): 
    t = np.arange(0,waktuAkhir,0.01)
    y = amplitudo * np.sin((2 * np.pi * frekuensi * t) + np.deg2rad(theta))
    return t,y

t1,y1 = sinusGenerator(1,1,4,0)
t2,y2 = sinusGenerator(1,1,4,90)
t3,y3 = sinusGenerator(1,1,4,180)

# membuat plot
dataplot1 = plt.plot(t1,y1)
dataplot2 = plt.plot(t2,y2)
dataplot3 = plt.plot(t3,y3)

plt.setp(dataplot1,color='r',linestyle='-',linewidth=1)
plt.setp(dataplot2,color='b',linestyle='-.',linewidth=2)
plt.setp(dataplot3,color='g',linestyle='--',linewidth=4)

# menampilkan plot
plt.show()