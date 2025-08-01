import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,10,20,30,40,50,60,70,80,90])
y = np.array([0,20,40,60,80,100,120,140,160,180])

font1 = {'family': 'Bahnschrift', 'size': 20 , 'color' : 'green' }
font2 = {'family': 'serif', 'size': 10 , 'color' : 'blue' }

plt.plot(x,y,)

plt.title("X,Y axes values",fontdict=font1, loc = 'left')

plt.xlabel("X position" , fontdict=font2)
plt.ylabel("Y position" , fontdict=font2)

plt.grid(axis='y',color='red', linestyle="--", linewidth=0.5)

plt.show()