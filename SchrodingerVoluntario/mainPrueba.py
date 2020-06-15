from schlib import *
from Plotting import plotEvolution, gifEvolution
from matplotlib import pyplot as plt

# Parámetros
n_ciclos = 10
N = 500
londa = 0.6
time = 200
fraction = int(time/100)

# Cálculo de constantes
k_0 = k0(n_ciclos, N)
s_param = s(k_0)
pot = V(londa, k_0, N)
onda = phiCero(k_0, N)
a = A(N, s_param, pot)
alfa_param = alfa(a, N)

# Algoritmo
x_esp = np.zeros(time, dtype=float)
p_esp = np.zeros(time, dtype=float)
xp_incer = np.zeros(time, dtype=float)
j = 0
for i in range(time):
    # Variables
    b_param = b(s_param, onda, N)       # Cálculo de parámetros
    beta_param = beta(N, a, alfa_param, b_param)
    xi_param = xi(N, alfa_param, beta_param)

    # Valores esperados
    # x_esp[i] = xEsperado(onda)
    # p_esp[i] = pEsperado(onda)

    # Principio incertidumbre
    xp_incer[i] = xIncertidumbre(onda)*pIncertidumbre(onda)

    # Representacion evolucion onda
    # if i % fraction == 0:
    #     plotEvolution(N, pot, pow(abs(onda), 2), norm(onda), x_esp[i], j)
    #     j += 1

    # Calculo onda en t+1
    onda = phi(onda, xi_param, N)


# Gif evolucion onda
# gifEvolution(time, fraction, n_ciclos)

# Representacion del valor esperado de x
# plt.plot(np.arange(start=0, stop=time, step=1, dtype=int), x_esp, "g")
# plt.xlabel("Tiempo (s)")
# plt.ylabel("Valor esperado de x")
# plt.title("Valor esperado de la posición en cada instante")
# plt.show()

# Representacion del valor esperado de p
# plt.plot(np.arange(start=0, stop=time, step=1, dtype=int), p_esp, "y")
# plt.xlabel("Tiempo (s)")
# plt.ylabel("Valor esperado de p")
# plt.title("Valor esperado del momento en cada instante")
# plt.show()

# Representacion para comprobacion P. Incertidumbre
# fig, ax = plt.subplots()
# plt.plot(np.arange(start=0, stop=time, step=1, dtype=int), xp_incer)
# plt.plot(np.arange(start=0, stop=time, step=1, dtype=int), np.ones(time, dtype=float)/2)
# plt.xlabel("Tiempo (s)")
# plt.ylabel("\u0394x\u0394p")
# plt.yticks([i/2 for i in range(1, 40) if (i % 6 == 0) or (i/2 == 1/2)])
# ax.set_yticklabels([str(i/2) for i in range(1, 40) if (i % 6 == 0) or (i/2 == 1/2)])
# plt.legend(["\u0394x\u0394p", "\u0127/2"])
# plt.title("Comprobación Principio de Incertidumbre")
# plt.show()
