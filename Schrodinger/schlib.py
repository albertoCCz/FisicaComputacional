import numpy as np
import math
import cmath


# Definimos las funciones que vamos a necesitar

# ^k0
def k0(n_ciclos, N):
    """
    Esta función calcula el valor del parámetro
    ^k_0, que es el número de onda reescalado
    :param n_ciclos:    # de ciclos de la f. de onda en el pozo
    :param N:           # de puntos a evaluar
    :return:            ^k0
    """
    return 2*math.pi*n_ciclos/N


# s
def s(k0):
    """
    Esta función calcula el valor del parámetro ^s
    :param k0:  número de onda reescalado
    :return:    ^s
    """
    return 1/(4*k0)


# V
def V(londa, k0, N):
    """
    Esta función devuelve un vector que contiene
    el valor del potencial en los distintos puntos
    del pozo
    :param londa:   -
    :param k0:      número de onda reescalado
    :param N:       # de puntos a evaluar
    :return:        numpy array v
    """
    v = np.zeros(N, dtype=float)

    for j in range(int(2*N/5), int(3*N/5)):
        v[j] = londa * k0**2

    return v


# norm
def norm(phi):
    """
    Esta función calcula la norma de la función
    de onda
    :param phi: función de onda phi
    :return:    norm (float number)
    """
    norm = math.sqrt(pow(abs(phi),2).sum())

    return norm


# phi(t)
def phiCero(k0, N):
    """
    Esta función calcula la función de onda inicial
    en cada punto del pozo
    :param k0:  número de onda reescalado
    :param N:   # de puntos a evaluar
    :return:    numpy array phi
    """
    phi = np.zeros(N+1, dtype=complex)

    for j in range(1, N-1):
        phi[j] = cmath.exp(complex(0, k0*j)) * cmath.exp(-8*((4*j-N)**2)/(N**2))


    return phi/norm(phi)


# A
def A(N, s, V):
    """
    Esta función calcula los tres parámetros
    A-,A0 y A+, que se devuelven como componentes
    de un array
    :param s:   param ^s
    :param V:   potencial V
    :return:    list of A coeffs
    """
    a_menos = np.ones(1, dtype=int)
    a_mas = np.ones(1, dtype=int)
    a0 = np.zeros(N, dtype=complex)

    for j in range(N):
        a0[j] = complex(-2-V[j], 2/s)

    return [a_menos, a0, a_mas]


# alfa
def alfa(A, N):
    """
    Esta función calcula el valor del parámetro
    alfa a partir de los coeficientes a_menos,
    a0 y a_mas
    :param A:   [a_menos,a0,a_mas]
    :param N:   # de puntos a evaluar
    :return:    numpy array alfa
    """
    alfa = np.zeros(N, dtype=complex)

    for i in range(N-2, -1,-1):
        alfa[i] = -A[0]/(A[1][i+1]+A[2]*alfa[i+1])

    return alfa


# b
def b(s, phi, N):
    """
    Esta función calcula el valor del parámetro
    b en cada punto del retículo para un instante
    de tiempo
    :param s:       param ^s
    :param phi:     función de onda phi
    :return:        numpy array b
    """
    b = np.zeros(N, dtype=complex)

    for i in range(N):
        b[i] = complex(0, 4*phi[i]/s)

    return b


# Beta
def beta(N, A, alfa, b):
    """
    Esta función calcula el valor del parámetro
    beta en cada punto del retículo para un instante
    de tiempo
    :param N:       # de puntos a evaluar
    :param A:       [a_menos,a0,a_mas]
    :param alfa:    param alfa
    :param b:       param b
    :return:        numpy array beta
    """
    beta = np.zeros(N, dtype=complex)

    for i in range(N-2, -1,-1):
        beta[i] = (b[i+1] - A[2] * beta[i+1]) / (A[1][i+1] + A[2] * alfa[i+1])

    return beta


# Xi
def xi(N, alfa, beta):
    """
    Esta función calcula el valor de xi en cada
    punto del retículo para un instante de tiempo
    :param N:       # de puntos a evaluar
    :param alfa:    param alfa
    :param beta:    param beta
    :return:        numpy array xi
    """
    xi = np.zeros(N+1, dtype=complex)

    for i in range(N):
        xi[i+1] = alfa[i] * xi[i] + beta[i]

    return xi


# phi
def phi(phi_prev, xi, N):
    """
    Esta función calcula la función de onda
    phi los puntos del retículo para el instante
    de tiempo t+1
    :param phi_prev:    f. de onda en t
    :param xi:          param xi
    :param N:           # de puntos a evaluar
    :return:            numpy array phi
    """
    phi = np.zeros(N+1, dtype=complex)

    for i in range(N+1):
        phi[i] = xi[i] - phi_prev[i]

    return phi
