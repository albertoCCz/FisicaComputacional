import numpy as np


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