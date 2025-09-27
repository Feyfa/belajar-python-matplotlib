import matplotlib.pyplot as plt
import numpy as np

# membuat data
def sinusGenerator(amplitudo,frekuensi,waktuAkhir,theta): 
    t = np.arange(0,waktuAkhir,0.01)
    y = amplitudo * np.sin((2 * np.pi * frekuensi * t) + np.deg2rad(theta))
    return t,y

t1,y1 = sinusGenerator(1,1,4,0)

# membuat plot
plt.plot(t1,y1)

# setting axis, minimum sama maximum, untuk setting panjang garis koordinat x dan y
# plt.axis([xmin,xmax,ymin,ymax])
plt.axis([0,4,-1.5,1.5]) 

# menampilkan plot
plt.show()