import matplotlib.pyplot as plt
import numpy as np
import random
import string

#vertical bar

plt.subplot(1,2,1)

x = np.array([random.choice(string.ascii_lowercase) for i in range(10)])
y = np.random.randint(1,20,size=10)

plt.bar(x,y,color="lime",width=0.75)
plt.title("Vertical Bar")
plt.xlabel("alphabets")
plt.ylabel("values")

#horizontal bar

plt.subplot(1,2,2)

x = np.array([random.choice(string.ascii_lowercase) for i in range(10)])
y = np.random.randint(1,20,size=10)


plt.barh(x,y,color="green",height=0.5)

plt.title("horizontal Bar")
plt.xlabel("alphabets")
plt.ylabel("values")



plt.show()
