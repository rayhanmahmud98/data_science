import random 
import matplotlib.pyplot as plt
import numpy as np

font1 = {'family': 'Bahnschrift', 'fontsize': 20, 'color': 'green'}
font2 = {'family': 'serif', 'fontsize': 10, 'color': 'blue'}



#plot1

x = np.random.randint(1,15,size=10)
y = np.random.randint(16,30,size=10)

plt.subplot(2,3,1)

plt.plot(x,y,)
plt.title("plot1")
plt.xlabel("X value",fontdict=font2)
plt.ylabel("Y value",fontdict=font2)

#plot2

x = np.random.randint(1,15,size=10)
y = np.random.randint(16,30,size=10)

plt.subplot(2,3,2)

plt.plot(x,y,)
plt.title("plot2")
plt.xlabel("X value",fontdict=font2)
plt.ylabel("Y value",fontdict=font2)


#plot3

x = np.random.randint(1,15,size=10)
y = np.random.randint(16,30,size=10)

plt.subplot(2,3,3)

plt.plot(x,y,)
plt.title("plot3")
plt.xlabel("X value",fontdict=font2)
plt.ylabel("Y value",fontdict=font2)


#plot4

x = np.random.randint(1,15,size=10)
y = np.random.randint(16,30,size=10)

plt.subplot(2,3,4)

plt.plot(x,y,)
plt.title("plot4")
plt.xlabel("X value",fontdict=font2)
plt.ylabel("Y value",fontdict=font2)


#plot5

x = np.random.randint(1,15,size=10)
y = np.random.randint(16,30,size=10)

plt.subplot(2,3,5)

plt.plot(x,y,)
plt.title("plot5")
plt.xlabel("X value",fontdict=font2)
plt.ylabel("Y value",fontdict=font2)


#plot6

x = np.random.randint(1,15,size=10)
y = np.random.randint(16,30,size=10)

plt.subplot(2,3,6)

plt.plot(x,y,)
plt.title("plot6")
plt.xlabel("X value",fontdict=font2)
plt.ylabel("Y value",fontdict=font2)


plt.suptitle("PLOT",fontdict=font1)
plt.show()
