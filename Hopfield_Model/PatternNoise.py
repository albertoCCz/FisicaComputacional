import numpy as np

dim = 20
num = 1
nLevel = 0.3

seed = 891651743
np.random.seed(seed)

def patternNoise(dim,num,nLevel):
    """
    This function randomly introduces noise in a given pattern
    :param dim: dimension N of the N^2 pattern array
    :param num: number represented by the pattern, integer [0,9]
    :param nLevel: noise level/ratio to introduce, [0,1)
    :return: noisy pattern. Numpy array with the same size as the pattern
    """
    # Open the pattern, "Dim<dim>_Num<num>.txt", and the noisy pattern
    p = np.loadtxt("Patterns/Dim" + str(dim) + "_Num" + str(num) + ".txt",
                   dtype=int,delimiter="\t")

    # Introducing noise
    for i in range(dim):
        for j in range(dim):
            rNum = np.random.random()
            if(rNum<nLevel):
                if(p[i][j] == 1):
                    p[i][j] *= 0
                else:
                    p[i][j] += 1

    # Saving the new created noisy pattern
    np.savetxt("PatternsNoisy/Dim" + str(dim) + "_Num" +
               str(num) + "_" + str(nLevel) + ".txt",X=p,
               fmt="%d",delimiter="\t",newline="\n")

    return print("Done with " + str(num) + "!")


patternNoise(dim,num,nLevel)
