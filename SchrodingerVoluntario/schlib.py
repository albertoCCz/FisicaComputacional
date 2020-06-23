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
    return 1/(4*k0**2)


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
    de onda, que realiza mediante la integración
    mediante la regla de Simpson
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


# Proceso de medida mediante proyeccion
def medicion(phi, N, detector="d"):
    """
    Calcula la probabilidad de que la particula
    sea medida por el detector
    :param phi:         función de onda phi
    :param N:           # de puntos a evaluar
    :param detector:    detector que realiza la medida
    :return:            P_detector
    """
    if detector == "i":
        inf = 0
        sup = int(N/5)
    else:
        inf = int(4*N/5)
        sup = N

    def proyeccion(phi):
        """
        Proyecta la función de onda si no es medida
        :param phi:         función de onda phi
        :return:            phi proyectada
        """
        phi[inf:sup] = complex(0, 0)

        return phi/norm(phi)

    prob = pow(abs(phi[inf:sup]), 2).sum()
    ran = np.random.random()

    if prob > ran:
        return True
    else:
        return proyeccion(phi)

# Calculo valores esperados
def xEsperado(phi):
    """
    Calcula el valor esperado de la posición
    para la función de onda phi
    :param phi:     función de onda phi
    :return:        x
    """
    x = np.arange(start=0, stop=len(phi), step=1, dtype=int)

    return (x * pow(abs(phi), 2)).sum()


def pEsperado(phi):
    """
    Calcula el valor esperado del momento
    de la funcion de onda phi
    :param phi:     funcion de onda phi
    :return:        p
    """
    return np.real(np.conjugate(phi) * complex(0, 1) * np.gradient(phi)).sum()


def x2Esperado(phi):
    """
    Calcula el valor esperado de x^2 para
    la funcion de onda phi
    :param phi:     funcion de onda phi
    :return:        x^2
    """
    x2 = np.square(np.arange(start=0, stop=len(phi), step=1, dtype=int))

    return (x2 * pow(abs(phi), 2)).sum()

def p2Esperado(phi):
    """
    Calcula el valor esperado de p^2 para
    la funcion de onda phi
    :param phi:     funcion de onda phi
    :return:        p^2
    """
    return np.real(- np.conjugate(phi) * np.gradient(np.gradient(phi))).sum()


def xIncertidumbre(phi):
    """
    Calcula la incertidumbre en x para
    la función de onda phi
    :param phi:     funcion de onda phi
    :return:        Delta(x)
    """
    return np.sqrt(x2Esperado(phi) - pow(xEsperado(phi), 2))


def pIncertidumbre(phi):
    """
    Calcula la incertidumbre en p para
    la funcion de onda phi
    :param phi:     funcion de onda phi
    :return:        Delta(p)
    """
    return np.sqrt(p2Esperado(phi) - pow(pEsperado(phi), 2))


def kineticEnergy(phi):
    """
    Calcula la energia cinetica de la
    onda en cada instante
    :param phi:     funcion de onda phi
    :return:        K
    """
    return np.real(- np.conjugate(phi) * np.gradient(np.gradient(phi))).sum()


def totalEnergy(phi, V0):
    """
    Calcula la energia total de la onda
    en cada instante
    :param phi:     funcion de onda phi
    :return:        Energia
    """
    return (V0 * pow(abs(phi[int(2*len(phi)/5) : int(3*len(phi)/5)]), 2)).sum() + kineticEnergy(phi)


def tCoefficient(k0, l_onda, N):
    """
    Calcula el coeficiente de transmision
    de la onda a traves de la barrera de
    potencial.
    :param k0:      # de onda reescalado
    :param l_onda:  longitud de onda
    :N:             # numero puntos grid
    :return:        T
    """
    v = l_onda * k0**2
    e = k0**2
    k_prima = math.sqrt(abs(e - v))
    if e < v:
        t = (1 + v**2 * np.sinh(k_prima * int(N/5))**2 / (4 * e * abs(e - v)))**(-1)
    elif e > v:
        t = (1 + v**2 * np.sin(k_prima * int(N/5))**2 / (4 * e * abs(e - v)))**(-1)
    else:
        t = "NaN"
    return t

