from schlib import *
from matplotlib import pyplot as plt

# Parámetros
n_ciclos = 10
N = 1000
londa = np.asarray([0.1, 0.3, 0.5, 1, 5, 10], dtype=float)
time = 200
fraction = int(time/(time/3))

# Algoritmo
l = 0
londa_len = len(londa)
prob = np.zeros((londa_len, time), dtype=float)
nd_max = np.zeros(londa_len, dtype=int)
prob_max = np.zeros(londa_len, dtype=float)
t_teorica = np.zeros(londa_len, dtype=float)

for j in range(londa_len):

    # Cálculo de constantes
    k_0 = k0(n_ciclos, N)
    s_param = s(k_0)
    pot = V(londa[j], k_0, N)
    onda = phiCero(k_0, N)
    a = A(N, s_param, pot)
    alfa_param = alfa(a, N)

    for i in range(time):
        b_param = b(s_param, onda, N)       # Cálculo de parámetros
        beta_param = beta(N, a, alfa_param, b_param)
        xi_param = xi(N, alfa_param, beta_param)

        prob[j][i] = pow(abs(onda[int(4*N/5):N]), 2).sum()

        onda = phi(onda, xi_param, N)       # Cálculo de onda en t+1

    nd_max[j] = np.where(prob[j] == np.max(prob[j]))[0][0]
    prob_max[j] = np.max(prob[j])

    # Calculo T teorica
    t_teorica[j] = tCoefficient(k_0, londa[j], N)

# Representamos la probabilidad en funcion del tiempo
# para cada lambda
# plt.plot(np.arange(time), prob[0])
# plt.plot(np.arange(time), prob[1])
# plt.plot(np.arange(time), prob[2])
# plt.plot(np.arange(time), prob[3])
# plt.plot(np.arange(time), prob[4])
# plt.plot(np.arange(time), prob[5])
# plt.xlabel("nD (s)")
# plt.ylabel("Probabilidad")
# plt.legend(["\u03BB = " + str(londa[i]) for i in range(londa_len)],
#            loc="upper right")
# plt.title("Probabilidad de encontrar la partícula en [4N/5, N]\nen función de nD")
# plt.show()

# Calculo T
print([f"Max_{londa[i]} = {max(prob[i])} con T = {t_teorica[i]}" for i in range(londa_len)])
