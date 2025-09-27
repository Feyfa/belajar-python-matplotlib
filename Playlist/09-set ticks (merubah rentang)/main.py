import matplotlib.pyplot as plt
import numpy as np

# membuat data
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))

plt.plot(sudut,y)

plt.ylabel('magnituda')
plt.xlabel('sudut')

plt.yticks([-1,0,1])
xtick_values = [0,90,180,270,360]
xtick_labels = [fr'$ {val}^o $' for val in xtick_values]
plt.xticks(xtick_values,xtick_labels)

plt.show()