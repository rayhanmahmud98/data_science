import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0,1,2,3,4,5,6,7,8]
y = [0,2,4,6,8,10,12,14,16]

plt.plot(x,y,label="2x",color="blue")

plt.title("Our First Title",color="blue")
plt.xlabel("X Axis",)
plt.ylabel("Y Axis")

plt.xticks([0,1,2,3,4,5,6,7])
plt.yticks([0,2,4,6,8,10,12,14])

plt.legend()

plt.show()