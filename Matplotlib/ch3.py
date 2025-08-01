from tkinter import Y
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,7,4,2,6,1,9])
xpoints = np.array([2,7,4,8,6,4,5])

plt.plot(ypoints , "o:r" , ms = 10 , mec = 'b', mfc = 'g',ls = 'dashed')
plt.plot(xpoints , "o:g" , ms = 10 , mec = 'g', mfc = 'c',ls = 'dotted')

plt.show()