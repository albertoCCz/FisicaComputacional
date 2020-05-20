from navelib import *
from plotSystem import plotSystem, gifSystem
import time

# Creamos el array de condiciones iniciales
phi0 = np.pi / 4.3
theta0 = np.pi / 4.3
v_esc = 11.2 * 1000 #m/s
perc = 0.99
v0 = perc * v_esc / constantes()[3]
h = 3
t = 0

y = np.zeros(4, dtype=float)
y[0] = constantes()[5] / constantes()[3]
y[1] = v0 * np.cos(theta0 - phi0)
y[2] = phi0
y[3] = y[0] * v0 * np.sin(theta0 - phi0)

# Algoritmo Runge-Kuta orden 4
n = 1000000
images = 250
start = time.time()
for i in range(n):
	k_1 =  k1(y, h, t)
	k_2 =  k2(k_1, y, h, t)
	k_3 =  k3(k_2, y, h, t)
	k_4 =  k4(k_3, y, h, t)

	if i % (n / images) == 0:
		plotSystem(y, t, i, hvalue(y, h, 1))

	y = yh(y, k_1, k_2, k_3, k_4)
	t 	+= hvalue(y, h, 1)

	if i % (n / 4) == 0:
		print(i / n * 100)


gifSystem(images)

end = time.time()
print(end-start)
