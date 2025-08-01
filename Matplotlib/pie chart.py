import matplotlib.pyplot as plt
import numpy as np
import random
import string

x = np.random.randint(1,10,size=10)

mylabels = np.array([random.choice(string.ascii_lowercase) for i in range(10)])
myexplode = [0.2, 0, 0.4, 0.5, 0, 0.3, 0.2, 0, 0.1, 0.2]
mycolors = ['red', 'green', 'blue', 'magenta', 'cyan', 'yellow', 'orange', 'purple', 'pink', 'brown']

plt.pie(x,labels=mylabels,startangle=90,explode=myexplode, shadow=True,colors=mycolors)
plt.legend(title="colors",loc='upper right')

plt.show()