import numpy as np;
import matplotlib.pyplot as plt










#MENCOBA MATPLOTLIB
# x = range(1,6)
# y = range(1,6)

# # kita membuat lingkaran
# radian360 = 2 * np.pi
# sudut = np.linspace(0, radian360, 5) # ini digunakan dari 0 - 2PHI itu di distribusikan sebanyak 100 bagian
# radius = 5

# x = radius * np.cos(sudut)
# y = radius * np.sin(sudut)

# # inisialisasi plot
# plt.plot(x,y)
# plt.show()
#MENCOBA MATPLOTLIB



















# KONSEP DASAR MEMBUAT LINGKARAN
# radius = 5
# radian360 = 2 * np.pi
# # buat figure
# plt.ion() # aktifkan interactive mode
# fig, ax = plt.subplots()
# for jumlah_titik in range(2, 361, 1):
#     sudut = np.linspace(0, radian360, jumlah_titik)
#     x = radius * np.cos(sudut)
#     y = radius * np.sin(sudut)

#     ax.clear()
#     ax.plot(x,y)
#     ax.set_title(f'Jumlah Titik : {jumlah_titik}')
#     ax.set_aspect('equal')
#     plt.draw()
#     plt.pause(0.1)
# input('test')
# KONSEP DASAR MEMBUAT LINGKARAN






# MEMBUAT SINUS
x = np.array([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10])
y = x ** 2

# jadi di plot ini maksud dari x dan y ini apasih??
# jadi saya punya function begini y = x^2. nah kalo saya punya x dari range -10 - 10. maka hasilnya akan menjadi seperti ini
# x   | y
# -10 | 100
#  -9 | 81 
#  -8 | 64 
#  -7 | 49 
#  -6 | 36
# begi terus sampai x = 10;
# jadi seperti itu konsep dari parameter x dan y, dengan begitu bisa membentuk sebuah garis yang sesuai perhitungan

plt.plot(x,y)
plt.grid()
plt.show()
# MEMBUAT SINUS











