from matplotlib import pyplot as plt
from RandPoint import dim,pasosMC
from ReDoPattern import npArray
from PIL import Image

f = open("Results/Dim" + str(dim) + "_Num" + str(1) +
         "_pasosMC" + str(pasosMC) + "_States.txt",)



plt.style.use("grayscale")

def plotSate(s,i):
    """
    Plot the new state of the system
    :param s: state to plot
    :return: image
    """
    fig, ax = plt.subplots()

    ax.imshow(s) # Representamos las figura
    ax.set_title(str(dim) + "x" + str(dim) + " and T=0.0001")    # Ponemos títulos

    fig.tight_layout()
    plt.savefig("Results/Prueba/Dim" + str(dim) + "_Num1" + "_pasosMC" +
                str(pasosMC) + str(i) + ".jpeg",quality=80,optimize=True,
                dpi=80,progressive=True,transparent=True)
    fig.clear()
    plt.close(fig)




# Generate all the images
images = []
for i in range(100):
    for j in range(dim):
        line = f.readline().split("\t")
        for k in range(dim):
            npArray[j][k] = line[k]
    plotSate(npArray, i)
    images.append(Image.open("Results/Prueba/Dim" + str(dim) +
                             "_Num1" + "_pasosMC" + str(pasosMC) +
                             str(i) + ".jpeg"))
    f.readline()


images[0].save("Results/Prueba/Dim" + str(dim) + "_Num1" +
               "_pasosMC" + str(pasosMC) + ".gif",
               save_all=True, append_images=images[1:],
               duration=100,loop=0)


