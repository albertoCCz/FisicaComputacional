from matplotlib import pyplot as plt
import numpy as np
from navelib import constantes
from PIL import Image


def plotSystem(y, t, j, h):
	"""
	Esta función representa el estado del
	sistema de 3 cuerpos
	:param y: 	Solución en t de las ecs. del mov.
	:param t: 	Tiempo
	:return: 	nada
	"""
	fig, ax = plt.subplots()
	r = y[0]
	phi = y[2]

	# Nave
	plt.plot(r*np.cos(phi), r*np.sin(phi), "ko", markersize=3)
	# Tierra
	plt.plot(0, 0, "co", markersize=5)
	# Luna
	plt.plot(np.cos(constantes()[4]*t), np.sin(constantes()[4]*t), "mo", markersize=3)

	# Eje X
	ax.set_xlabel("Distancia [en d_TL]")
	# ax.set_xticks([i/10-1for i in range(21) if i % 2 == 0])
	# ax.set_xticklabels([str(i/10-1) for i in range(21) if i % 2 == 0])
	ax.set_xlim(xmin=-1.1, xmax=1.1)
	# Eje Y
	ax.set_ylabel("Distancia [en d_TL]")
	# ax.set_yticks([i/10-1 for i in range(21) if i % 2 == 0])
	# ax.set_yticklabels([str(i/10-1) for i in range(21) if i % 2 == 0])
	ax.set_ylim(ymin=-1.1, ymax=1.1)
	# Otros
	plt.title("'Fly me to the Moon'\nmediante Runge-Kuta orden 4\nh = " + str(h))
	# Guardamos la imagen
	plt.savefig("Resultados/Imagenes/" + str(int(j/4000)) + ".png",
				optimize=True, dpi=100, progressive=True)
	plt.close(fig)
	fig.clear()


def gifSystem(n):
	images = []
	for i in range(n):
		images.append(Image.open("Resultados/Imagenes/" +
                                 str(i) + ".png"))

	images[0].save("Resultados/Gifs/Prueba_10_" + str(n) + ".gif",
                   save_all=True, append_images=images[1:],
                   duration=100, loop=0)
