import numpy as np
import matplotlib.pyplot as plt

"""
    1. membuat data
    2. membuat plot
    3. menampilkan plot
"""

# 1. membuat data
# rumus nya (sin(2wt + theta)) atau (A . sin(2 . PHI . f . t + theta))
def sinusGenerator(amplitudo,frekuensi,waktuAkhir,theta): 
    t = np.arange(0,waktuAkhir,0.025)
    y = amplitudo * np.sin((2 * np.pi * frekuensi * t) + np.deg2rad(theta))
    return t,y

# 2. membuat plot 
t1,y1 = sinusGenerator(1,1,4,0)
plt.plot(t1,y1)

t2,y2 = sinusGenerator(1,1,4,30)
plt.plot(t2,y2,'r')

t3,y3 = sinusGenerator(1,1,4,60)
plt.plot(t3,y3,'b--')

t4,y4 = sinusGenerator(1,1,4,90)
# formatnya 'warna-huruf'
plt.plot(t4,y4,'c-o')

# 3. membuat plot
plt.show()