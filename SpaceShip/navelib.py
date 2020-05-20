import numpy as np


# Funciones que vamos a necesitar


def constantes():
	"""
	Devuelve en un array el valor de las siguientes
	constantes físicas:
	G, M_T, M_L, d_TL, w, R_T, R_L
	:return:		G, M_T, M_L, d_TL, w, R_T, R_L
	"""

	return [6.67e-11, 5.9736e24, 0.07349e24,
			3.844e8, 2.6617e-6, 6.378160e6,
			1.7374e6]


def delta():
	"""
	Calcula el valor de la constante Delta
	:return: 		Delta
	"""

	return constantes()[0] * constantes()[1] / constantes()[3]**3


def mu():
	"""
	Calcula el ratio de masas Tierra-Luna
	:return: 		mu
	"""

	return constantes()[2] / constantes()[1]


def rPrima(r, phi, t):
	"""
	Calcula r'
	:param r:		Coordenada radial cohete (reescalada)
	:param phi:		Coordenada angular cohete
	:param t:		Tiempo
	:return:		r'
	"""

	return np.sqrt(1 + r ** 2 - 2 * r * np.cos(phi - constantes()[4] * t))


def rPunto(p_r):
	"""
	Calcula la derivada de la coordenada radial cochete
	:param p_r: 	Momento radial cohete
	:return: 		r_punto
	"""

	return p_r


def rMPunto(phiM, r, rPrima, phi, t):
	"""
	Calcula la derivada del momento de la coordenada
	radial cohete
	:param phiM: 	Momento coord. angular cohete
	:param r: 		Coordenada radial cohete
	:param phi: 	Coordenada angular cohete
	:param t: 		Tiempo
	:return:		rM_punto
	"""

	return phiM**2/r**3 - delta() *\
		   (1/r**2 + mu()/rPrima**3 * (r - np.cos(phi - constantes()[4] * t)))


def phiPunto(phiM, r):
	"""
	Calcula la derivada de la coordenada angular
	cohete
	:param phiM: 	Momento coord. angular cohete
	:param r: 		Coordenada radial cohete
	:return: 		phi_punto
	"""

	return phiM / r**2


def phiMPunto(r, phi, rPrima, t):
	"""
	Calcula la derivada del momento de la coordenada
	angular
	:param r: 		Coordenada radial cohete
	:param phi: 	Coordenada angular cohete
	:param rPrima: 	r'
	:param t:		Tiempo
	:return:		phiM_punto
	"""

	return -delta() * mu() * r / rPrima**3 * np.sin(phi - constantes()[4]*t)


def k1(y, h, t):
	"""
	Calcula k1 para cada f_i
	:param y:		array([y1 y2 y3 y4])
	:param h: 		Paso temporal
	:param t: 		Tiempo
	:return: 		[k11, k12, k13, k14]
	"""
	k_1 = np.zeros(4, dtype=float)

	k_1[0] = h * rPunto(y[1])
	k_1[1] = h * rMPunto(y[3], y[0], rPrima(y[0], y[2], t), y[2], t)
	k_1[2] = h * phiPunto(y[3], y[0])
	k_1[3] = h * phiMPunto(y[0], y[2], rPrima(y[0], y[2], t), t)

	return k_1


def k2(k1, y, h, t):
	"""
	Calcula k2 para cada f_i
	:param y:		array([y1 y2 y3 y4])
	:param h: 		Paso temporal
	:param t: 		Tiempo
	:return:		[k21, k22, k23, k24]
	"""
	k_1 = k1/2
	t = t+h/2
	k_2 = np.zeros(4, dtype=float)

	k_2[0] = h * rPunto(y[1]+k_1[1])
	k_2[1] = h * rMPunto(y[3]+k_1[3], y[0]+k_1[0],
						 rPrima(y[0]+k_1[0], y[2]+k_1[2], t), y[2]+k_1[2], t)
	k_2[2] = h * phiPunto(y[3]+k_1[3], y[0]+k_1[0])
	k_2[3] = h * phiMPunto(y[0]+k_1[0], y[2]+k_1[2],
						   rPrima(y[0]+k_1[0], y[2]+k_1[2], t), t)

	return k_2


def k3(k2, y, h, t):
	"""
	Calcula k3 para cada f_i
	:param y:		array([y1 y2 y3 y4])
	:param h: 		Paso temporal
	:param t: 		Tiempo
	:return:		[k31, k32, k33, k34]
	"""
	k_2 = k2/2
	t = t+h/2
	k_3 = np.zeros(4, dtype=float)

	k_3[0] = h * rPunto(y[1]+k_2[1])
	k_3[1] = h * rMPunto(y[3]+k_2[3], y[0]+k_2[0],
						 rPrima(y[0]+k_2[0], y[2]+k_2[2], t), y[2]+k_2[2], t)
	k_3[2] = h * phiPunto(y[3]+k_2[3], y[0]+k_2[0])
	k_3[3] = h * phiMPunto(y[0]+k_2[0], y[2]+k_2[2],
						   rPrima(y[0]+k_2[0], y[2]+k_2[2], t), t)

	return k_3


def k4(k_3, y, h, t):
	"""
	Calcula k4 para cada f_i
	:param y:		array([y1 y2 y3 y4])
	:param h: 		Paso temporal
	:param t: 		Tiempo
	:return:		[k31, k32, k33, k34]
	"""
	t = t+h
	k_4 = np.zeros(4, dtype=float)

	k_4[0] = h * rPunto(y[1]+k_3[1])
	k_4[1] = h * rMPunto(y[3]+k_3[3], y[0]+k_3[0],
						 rPrima(y[0]+k_3[0], y[2]+k_3[2], t), y[2]+k_3[2], t)
	k_4[2] = h * phiPunto(y[3]+k_3[3], y[0]+k_3[0])
	k_4[3] = h * phiMPunto(y[0]+k_3[0], y[2]+k_3[2],
						   rPrima(y[0]+k_3[0], y[2]+k_3[2], t), t)

	return k_4


def yh(y, k1, k2, k3, k4):
	"""
	Calcula las ecuaciones dinámicas en instante
	t + h
	:param y:		array([y1 y2 y3 y4])
	:param k1: 		k1
	:param k2: 		k2
	:param k3: 		k3
	:param k4: 		k4
	:return: 		y_n(t+h)
	"""
	yh = np.zeros(4, dtype=float)

	for i in range(4):
		yh[i] = y[i] + 1/6 * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i])

	return yh


def hvalue(y, h, m):

	# Método 1
	if m == 1 and y[0] > 0.95:
		h = 0.5
	# Método 2
	if m == 2 and y[3] > 0:
		h = 0.5

	return h
