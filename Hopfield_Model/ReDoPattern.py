import numpy as np
from RandPoint import dim

f = open("Patterns/Numeros/1.txt","r")
g = open("Patterns/Numeros/1New.txt","w")

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
