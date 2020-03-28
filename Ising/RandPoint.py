import numpy.random as npr
from RandState import dim
from RandState import seed

npr.seed(seed)  #set seed

f = open("RandPoints_" + str(seed) + ".txt","w")

timeLim = 100 * dim**2 #tiempo de ejecucion (en unidades de N^2)

i = 0
while(i<timeLim):
    x = npr.randint(0,dim)
    y = npr.randint(0,dim)
    sigma = npr.random()
    f.write(str(x) + "\t" + str(y) + "\t" + str(sigma) + "\n")

    i += 1
