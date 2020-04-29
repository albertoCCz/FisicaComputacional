"""import numpy as np


# Set pattern
num = 1
s = np.array([[0, 0, 1, 0, 0],
             [0, 1, 1, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 1, 1, 1, 0]])

dim = len(s[0])

# Save pattern
f = open("Patterns/Dim" + str(dim) + "_Num" + str(num) + ".txt","w")

for i in range(dim):
    for j in range(dim):
        f.write(str(s[i][j]))
        if((j+1)%5==0):
            f.write("\n")
        else:
            f.write("\t")
"""

import numpy.random as npr

dim = 50
seed = 891651743

f = open("PatternsNoisy/Pruebas/RandomNoise" + str(dim) + ".txt","w")

npr.seed(seed) #set seed
s = npr.choice([0,1],(dim,dim))    #generates the sample

for i in range(dim):
    for j in range(dim):
        f.write(str(s[i][j]))
        if((j+1) % dim == 0):
            f.write("\n")
        else:
            f.write("\t")

