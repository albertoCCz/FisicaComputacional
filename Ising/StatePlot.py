from matplotlib import pyplot as plt
from RandState import s,seed,dim #get initial state from RandState.py
from PIL import Image


f = open("Systems/" + str(dim) + "_" + str(seed) + "/StateChanges_" + str(seed) + ".txt","r")
plt.style.use("classic")

def plotSate(s,i,seed):
    """
    Plot the new state of the system
    :param s: state to plot
    :return: image
    """
    fig, ax = plt.subplots()

    im = ax.imshow(s)

    plt.xticks([i for i in range(dim)], "")
    plt.yticks([i for i in range(dim)], "")

    fig.tight_layout()
    plt.savefig("Systems/" + str(dim) + "_" + str(seed) + "/Images/" + str(i) +
                ".jpeg",quality=80,optimize=True,
                dpi=80,progressive=True,transparent=True)
    fig.clear()
    plt.close(fig)


#Generate all the images
images = []
for i in range(99):
    f.readline()
    for j in range(dim):
        line = f.readline().split("\t")
        for k in range(dim):
            s[j][k] = line[k]
    plotSate(s,i,seed)
    images.append(Image.open("Systems/" + str(dim) + "_" +
                             str(seed) + "/Images/" + str(i) + ".jpeg"))

images[0].save("Systems/" + str(dim) + "_" + str(seed) + "/Images/State_" +
               str(dim) + "_" + str(seed) + ".gif",save_all=True,
               append_images=images[1:],duration=100)

