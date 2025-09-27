import matplotlib.pyplot as plt
import numpy as np

# membuat data
def sinusGenerator(amplitudo,frekuensi,waktuAkhir,theta): 
    t = np.arange(0,waktuAkhir,0.01)
    y = amplitudo * np.sin((2 * np.pi * frekuensi * t) + np.deg2rad(theta))
    return t,y

amplitudo = 1
frekuensi = 1
waktuAkhir = 4
theta = 0

t1,y1 = sinusGenerator(amplitudo,frekuensi,waktuAkhir,theta)

# membuat plot
plt.plot(t1,y1)

judul = 'Grafik Sinusoidal\n'
rumus = r'$ \mathcal{Y} = A sin(2 \omega t + \theta)$' + '\n'
parameter1 = fr'$ A = {amplitudo} cm , \omega = {frekuensi} \mathit{{Hz}} , \theta = {theta} ^{'o'} $'

plt.title(judul + rumus + parameter1)
plt.xlabel(f'waktu(detik)')
plt.ylabel(f'magnituda(cm)')

# menampilkan plot
plt.show()

