from matplotlib import pyplot as plt
from RandPoint import dim,pasosMC

name1 = "PatternsNoisy"
name2 = "Homer0.005"
name3 = "Homer0.05"
name4 = "Homer0.5"

f = open("Results/Dim" + str(dim) + "_" + name1 +
         "_pasosMC" + str(pasosMC) + "_Solap.txt","r")
"""
g = open("Results/Dim" + str(dim) + "_" + name2 +
         "_pasosMC" + str(pasosMC) + "_Solap.txt","r")
h = open("Results/Dim" + str(dim) + "_" + name3 +
         "_pasosMC" + str(pasosMC) + "_Solap.txt","r")
m = open("Results/Dim" + str(dim) + "_" + name4 +
         "_pasosMC" + str(pasosMC) + "_Solap.txt","r")
"""

# Ploteamos el solapamiento
solap = [[],[],[],[],[],[]]
paso = []
for i in range(1000):
    line1 = f.readline().split("\t")
    paso.append(float(line1[0]))
    for j in range(6):
        solap[j].append(float(line1[j+1]))
    """
    line2 = g.readline().split("\t")
    line3 = h.readline().split("\t")
    line4 = m.readline().split("\t")
    solap[1].append(float(line2[0]))
    solap[2].append(float(line3[0]))
    solap[3].append(float(line4[0]))
    """


fig, ax = plt.subplots()
ax.plot(paso,solap[0],linewidth=2)
ax.plot(paso,solap[1],linewidth=2)
ax.plot(paso,solap[2],linewidth=2)
ax.plot(paso,solap[3],linewidth=2)
ax.plot(paso,solap[4],linewidth=2)
ax.plot(paso,solap[5],linewidth=2)
ax.set_xlim(left=0,right=20)
ax.set_ylim(bottom=-1.2,top=1.2)
ax.set_xticks([i for i in range(pasosMC+1) if i%2 == 0])
ax.set_xticklabels([str(i) for i in range(pasosMC+1) if i%2 == 0])
ax.set_yticks([-1,0,1])
ax.set_yticklabels(["-1","0","1"])
ax.set_title("Solapamiento con el patrón en función del tiempo")
ax.set_xlabel("Tiempo (en pasos MC)")
ax.set_ylabel("Solapamiento")
plt.legend(["Github","Homer","Kim","Nietzsche", "Python","Trump"])
plt.show()
