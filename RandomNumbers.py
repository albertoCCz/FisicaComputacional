import random

for i in range(0,10000,1):
    random.seed(1+i)
    x = random.random()
    random.seed(102+i)
    y = random.random()
    print(str(x) + "\t" + str(y))
