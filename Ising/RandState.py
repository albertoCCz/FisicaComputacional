import numpy.random as npr

seed = 6531898  #seed of this sample
dim = 10

f = open("RandState_" + str(seed) + ".txt",'w')   #file to save initial data

npr.seed(seed) #set seed
x = npr.choice([-1,1],(dim,dim))    #generates the sample

for i in range(dim):
    for j in range(dim):
        f.write(str(x[i][j]))
        if((j+1) % dim == 0):
            f.write("\n")
        else:
            f.write("\t")
