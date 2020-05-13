from schlib import *
from Plotting import plotEvolution, gifEvolution


# Parámetros
n_ciclos = 50
N = 500
londa = 0.2
time = 10000
fraction = int(time/250)

# Cálculo de constantes
k_0 = k0(n_ciclos, N)
s_param = s(k_0)
pot = V(londa, k_0, N)
onda = phiCero(k_0, N)
a = A(N, s_param, pot)
alfa_param = alfa(a, N)

# Algoritmo
j = 0
for i in range(time):
    b_param = b(s_param, onda, N)       # Cálculo de parámetros
    beta_param = beta(N, a, alfa_param, b_param)
    xi_param = xi(N, alfa_param, beta_param)

    if i % fraction == 0:
        plotEvolution(N, pot, pow(abs(onda), 2), norm(onda), j)
        j += 1

    onda = phi(onda, xi_param, N)       # Cálculo de onda en t+1

gifEvolution(N, time, fraction, n_ciclos)
