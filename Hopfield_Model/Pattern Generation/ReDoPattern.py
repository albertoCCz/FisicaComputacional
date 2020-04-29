import numpy as np
from RandPoint import dim

name = "Trump"

f = open("Patterns/Pruebas/Images/" + str(name) + ".txt","r")
g = open("Patterns/Pruebas/Images/" + str(name) + "New.txt","w")

def split(texto):
    lista = [int(char) for char in texto if(char == '0' or char == '1')]
    return lista

lista = []
for i in range(dim):
    lista.append([])
    lista[i] = split(f.readline())

npArray = np.asarray(lista,dtype=np.int)

for i in range(dim):
    for j in range(dim):
        g.write(str(npArray[i][j]))
        if((j+1 == dim)):
            g.write("\n")
        else:
            g.write("\t")
