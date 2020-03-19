from matplotlib import pyplot as plt
import numpy as np

f = open("Posiciones.txt","r")  #open data file

N = 40001   #number of points for each one
n = 9       #number of objects (8 planets + the Sun)
x = np.zeros((n,N))
y = np.zeros((n,N))

#read the file and save the data
for i in range(N):
    lineList = f.readline().split()
    for j in range(n):
        x[j][i], y[j][i] = lineList[2*j], lineList[2*j+1]

#plot the orbits
for i in range(n):
    plt.plot(x[i],y[i])
plt.xlabel("r_x (UA)")
plt.ylabel("r_y (UA)")
plt.title("Órbitas planetas Sistema Solar")
plt.grid()
plt.show()
