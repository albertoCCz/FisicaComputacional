from schlib import *
from matplotlib import pyplot as plt

# Parámetros
n_ciclos = 10
N = np.asarray([500, 1000, 2000], dtype=int)
londa = 0.6
time = 200
fraction = int(time/(time/3))

# Algoritmo
N_len = len(N)
prob = np.zeros((N_len, time), dtype=float)
nd_max = np.zeros(N_len, dtype=int)
prob_max = np.zeros(N_len, dtype=float)

for j in range(N_len):

    # Cálculo de constantes
    k_0 = k0(n_ciclos, N[j])
    s_param = s(k_0)
    pot = V(londa, k_0, N[j])
    onda = phiCero(k_0, N[j])
    a = A(N[j], s_param, pot)
    alfa_param = alfa(a, N[j])

    for i in range(time):
        b_param = b(s_param, onda, N[j])       # Cálculo de parámetros
        beta_param = beta(N[j], a, alfa_param, b_param)
        xi_param = xi(N[j], alfa_param, beta_param)

        prob[j][i] = pow(abs(onda[int(4*N[j]/5):N[j]]), 2).sum()

        onda = phi(onda, xi_param, N[j])       # Cálculo de onda en t+1

    nd_max[j] = np.where(prob[j] == np.max(prob[j]))[0][0]
    prob_max[j] = np.max(prob[j])

# Representamos la probabilidad en funcion del tiempo
# para cada lambda
plt.plot(np.arange(time), prob[0], ".")
plt.plot(np.arange(time), prob[1], "-")
plt.plot(np.arange(time), prob[2], "--")
plt.xlabel("nD (s)")
plt.ylabel("Probabilidad")
plt.legend(["N = " + str(N[i]) for i in range(N_len)],
           loc="upper right")
plt.title("Probabilidad de encontrar la partícula en [4N/5, N]\nen función de nD")
plt.show()
print([f"Max_{N[i]} = {prob_max[i]}" for i in range(N_len)])
