import random

for i in range(0,100000,1):
    random.seed(1+i)
    x = random.random()-1/2
    random.seed(102+i)
    y = random.random()-1/2
    print(str(x) + "\t" + str(y))
