from matplotlib import pyplot as plt
from PIL import Image


def plotEvolution(N, pot, modOnda, norm, x_esp, i):
    fig, ax = plt.subplots()
    # Plot
    plt.fill_between([i for i in range(N)], pot,
                     color='lightblue', alpha=0.4)
    plt.fill_between([i for i in range(N + 1)], modOnda,
                     color='salmon', alpha=0.6)
    plt.plot(x_esp, pot[int(N/2)]/2, "b+", markersize=4)
    # Eje X
    ax.set_xticks([i for i in range(N + 1) if i % (int(N/10)) == 0])
    ax.set_xticklabels([str(i) for i in range(N + 1) if i % (int(N/10)) == 0])
    ax.set_xlabel("Posición")
    # Eje Y
    ax.set_yticks([i / 100 for i in range(15) if i % 4 == 0])
    ax.set_yticklabels([str(i / 100) for i in range(15) if i % 4 == 0])
    ax.set_ylabel("Densidad de probabilidad")
    # Otros ajustes
    plt.legend(["x Esperado  ;  Iteration:" + str(i), "V(x)", "|phi(x)|^2 with norm = " + str(norm)])
    ax.set_title("Ecuación Shrödinger 1D\nen potencial cuadrado infinito")
    # Guardamos plot
    plt.savefig("Resultados/Representaciones/Imagenes/" +
                str(i) + ".jpeg", optimize=True,
                dpi=80, progressive=True)
    plt.close(fig)
    fig.clear()


def gifEvolution(time, fraction, n_ciclos):
    images = []
    for i in range(int(time/fraction)):
        images.append(Image.open("Resultados/Representaciones/Imagenes/" +
                                 str(i) + ".jpeg"))

    images[0].save("Resultados/Representaciones/Gifs/" + str(time) + "_" + str(n_ciclos) + ".gif",
                   save_all=True, append_images=images[1:],
                   duration=120, loop=0)
