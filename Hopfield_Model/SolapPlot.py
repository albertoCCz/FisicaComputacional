from matplotlib import pyplot as plt
from RandPoint import dim,pasosMC

g = open("Results/Dim" + str(dim) + "_Num" + str(1) +
         "_pasosMC" + str(pasosMC) + "_Solap.txt",)

# Ploteamos el solapamiento
solap = []
paso = []
for i in range(1000):
    line = g.readline().split("\t")
    solap.append(float(line[0]))
    paso.append(float(line[1]))


fig, ax = plt.subplots()
ax.plot(paso,solap,"c-.",linewidth=2)
ax.set_xlim(left=0,right=20)
ax.set_ylim(bottom=-1.2,top=1.2)
ax.set_xticks([i+1 for i in range(20)])
ax.set_xticklabels([str(i+1) for i in range(20)])
ax.set_yticks([-1,0,1])
ax.set_yticklabels(["-1","0","1"])
ax.set_title("Solapamiento con patrones en función del tiempo")
ax.set_xlabel("Tiempo (en pasos MC)")
ax.set_ylabel("Solapamiento")
plt.legend(["Patrón 1"])
plt.show()
