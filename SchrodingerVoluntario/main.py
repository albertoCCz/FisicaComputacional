from schlib import *
import time


# Parámetros
n_ciclos = 10
N = 500
londa = 0.6
tiempo = 120
nd = 9
fraction = int(tiempo/250)

# Cálculo de constantes
k_0 = k0(n_ciclos, N)
s_param = s(k_0)
pot = V(londa, k_0, N)
a = A(N, s_param, pot)
alfa_param = alfa(a, N)

# Reproducibilidad
np.random.seed(65758)

# Algoritmo
nsim = 1
mt = 0
for sim in range(nsim):
    start = time.time()
    onda = phiCero(k_0, N)
    for i in range(tiempo):
        b_param = b(s_param, onda, N)       # Cálculo de parámetros
        beta_param = beta(N, a, alfa_param, b_param)
        xi_param = xi(N, alfa_param, beta_param)

        onda = phi(onda, xi_param, N)  # Cálculo de onda en t+1

        if i % int(tiempo / nd) == 0:
            if i == tiempo - 1:
                print(i)

            medD = medicion(onda, N, detector="d")

            if medD is True:
                mt += 1
                break
            else:
                onda = medD
                medI = medicion(onda, N, detector="i")

                if medI is True:
                    break
                else:
                    onda = medI

    if sim % int(nsim/4) == 0:
        print("Completado: " + str(int(sim/nsim*100)) + "%\t;\tmt = " + str(mt))

    # finish = time.time()
    # print("Tiempo simulación = " + str(finish - start))

print("mt total: " + str(mt) + "\t;\tK = mt/#Simulaciones = " + str(mt/nsim))
