import random
import matplotlib.pyplot as plt
import numpy as np

#day1

x = np.random.randint(1,10,size=10)
y = np.random.randint(50,100,size=10)

colors = np.random.randint(1,100,size=10)

plt.scatter(x,y,c = colors, cmap = 'viridis')
plt.colorbar()

#day2

x = np.random.randint(1,10,size=10)
y = np.random.randint(50,100,size=10)

colors = np.random.randint(1,100,size=10)

plt.scatter(x,y,c = colors, cmap = 'turbo_r')
plt.colorbar()

#day3

x = np.random.randint(1,10,size=10)
y = np.random.randint(50,100,size=10)


colors = np.random.randint(1,100,size=10)

plt.scatter(x,y,c = colors, cmap = 'BuPu_r')
plt.colorbar()

plt.show()