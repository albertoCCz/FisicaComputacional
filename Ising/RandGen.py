import numpy as np

seed = 6531898  #seed of this sample
dim = 10

f = open("RandState" + str(seed) + ".txt",'w')   #file to save initial data

np.random.seed(seed) #set seed
x = np.random.choice([-1,1],(dim,dim))    #generates the sample

for i in range(dim):
    for j in range(dim):
        f.write(str(x[i][j]))
        if((j+1) % dim == 0):
            f.write("\n")
        else:
            f.write("\t")
