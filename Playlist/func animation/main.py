# import
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# import


# data melengkung
x = np.arange(-10,11,0.1)
y = (x ** 2)
# data melengkung


# mendapatkan figure(kertas gambar) dan ax(sumbu x-y tempat menggambar)
fig, ax = plt.subplots()
# mendapatkan figure(kertas gambar) dan ax(sumbu x-y tempat menggambar)


# setting panjang x dan y
ax.set_xlim(-10,10)
ax.set_ylim(0,100)
# setting panjang x dan y


# geser position garis koorinat
ax.spines['left'].set_position(('data', 0))   # Y-axis di x=0
ax.spines['bottom'].set_position(('data', 0)) # X-axis di y=0
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none') 
# geser position garis koorinat 


# Hilangkan label "0" di sumbu Y
yticks = ax.get_yticks()
ax.set_yticklabels([None if tick == 0 else int(tick) for tick in yticks])
# Hilangkan label "0" di sumbu Y


# buat plot dengan isi kosong
line, = plt.plot([],[],'r')
# buat plot dengan isi kosong


# setup untuk membuat animasi
frames = (x.size + 1) # berapa banyak titik koordinat, biasanya jumlah titik nya ditambah 1
interval = 40 # delay 40ms
anim = FuncAnimation(
    fig=fig,
    func=lambda frame: (
        # print(frame),
        line.set_data(x[:frame],y[:frame]), # nanti bakal ambil x dan y sesuai panjang dari index nya, misal index nya ke 2, maka nilai x jadi [e1,e2,e3]. begitupun dengan y
        line
    )[-1],
    frames=frames,
    interval=interval
)
# setup untuk membuat animasi


# munculkan plot
plt.show()
# munculkan plot