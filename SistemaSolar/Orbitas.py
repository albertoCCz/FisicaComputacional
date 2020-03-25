from matplotlib import pyplot as plt
import numpy as np

f = open("Posiciones.txt","r")

N = 20001
n = 9
x = np.zeros((n,N))
y = np.zeros((n,N))
space = np.linspace(1,N,N)
eCin = []
ePot = []
eTot = []

for i in range(N):
    lineList = f.readline().split()
    eCin.append(float(lineList[-2]))
    ePot.append(float(lineList[-1]))
    eTot.append(float(eCin[i])+float(ePot[i]))

    for j in range(n):
        x[j][i], y[j][i] = lineList[2*j], lineList[2*j+1]

"""
for i in range(n):
    plt.plot(x[i],y[i])
plt.xlabel("r_x (UA)")
plt.ylabel("r_y (UA)")
plt.legend(["Sol", "Mercurio", "Venus", "Tierra",
            "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"])
plt.title("Órbitas planetas relativas a la Tierra")
plt.grid()
"""
plt.grid()
plt.title("Conservación Energía Sistema Solar")
plt.plot(space,eCin)
plt.plot(space,ePot)
plt.plot(space,eTot)
plt.legend(["Cinética","Potencial","Total"])
plt.ylabel("Energía")
plt.xlabel("Iteración/1000")

plt.show()
