from matplotlib import pyplot as plt
from RandState import s,seed #get initial state from RandState.py
from PIL import Image
from RandPoint import timeLim

f = open("StateChanges_" + str(seed) + ".txt","r")


def plotSate(s,i,seed):
    """
    Plot the new state of the system
    :param s: state to plot
    :return: image
    """
    fig, ax = plt.subplots()
    im = ax.imshow(s)

    plt.xticks([i for i in range(10)], "")
    plt.yticks([i for i in range(10)], "")

    fig.tight_layout()
    plt.savefig("StateImages/Seed_" + str(seed) + "/State_" + str(i) +
                "_" + str(seed) + ".jpeg")
    fig.clear()
    plt.close(fig)


#Generate all the images
images = []
for i in range(8185):
    #plotSate(s, i, seed)
    line = f.readline().split("\t")
    s[int(line[0])][int(line[1])] = line[2]
    images.append(Image.open("StateImages/Seed_" + str(seed) +
                             "/State_" + str(i) + "_" +
                             str(seed) + ".jpeg"))

images[0].save("StateImages/Seed_" + str(seed) + "/States_" + str(seed) + ".gif",save_all=True,
               append_images=images[1:],duration=10)

