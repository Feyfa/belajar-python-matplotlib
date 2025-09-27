import matplotlib.pyplot as plt
import numpy as np

# membuat data
def sinusGenerator(amplitudo,frekuensi,waktuAkhir,theta): 
    t = np.arange(0,waktuAkhir,0.01)
    y = amplitudo * np.sin((2 * np.pi * frekuensi * t) + np.deg2rad(theta))
    return t,y

t1,y1 = sinusGenerator(1,1,4,0)

plt.plot(t1, y1)

# plt.text(x,y,message)
plt.text(1.6,1.2,r'$ y = \mathcal{A}.sin(2 \omega t) $')


plt.show()