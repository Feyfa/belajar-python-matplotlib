import numpy as np
import matplotlib.pyplot as plt

"""
    1. membuat data
    2. membuat plot
    3. menampilkan plot
"""

# 1. membuat data
x = np.array([1,2,3,4,5])
y = x ** 2
y2 = y ** 2

# 2. membuat plot
plt.plot(x, y)
plt.plot(x, y2)

# 3. menampilkan plot
plt.show()