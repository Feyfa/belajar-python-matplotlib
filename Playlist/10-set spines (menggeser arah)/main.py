import matplotlib.pyplot as plt
import numpy as np

# membuat data 
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))

plt.plot(sudut,y)
plt.title('Grafis Sinusoidal')
plt.text(190,1,'magnituda')
plt.text(360,0.1,'sudut')

plt.yticks(np.arange(-1,1.5,0.5))
xtick_values = [0,90,180,270,360]
xtick_labels = [fr'$ {val}^o $' for val in xtick_values]
plt.xticks(xtick_values,xtick_labels)

ax = plt.gca()
ax.spines['left'].set_position(('data',180))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()