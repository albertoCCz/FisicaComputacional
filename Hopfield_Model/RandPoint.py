import numpy as np

dim = 20    # Pattern dimension
N = dim*dim # Number of neurons
pasosMC = 20    # Number of Monte Carlo steps

# Create file to save data
f = open("Iteraciones/Dim" + str(dim) + "_pasosMC" + str(pasosMC) + ".txt","w")

# Generamos los puntos y le asociamos un numero entre 0 y 1
iteraciones = N*pasosMC   # numero de iteraciones = numero de pasos Monte Carlo

i = 0
while(i<iteraciones):
    p = np.random.randint(0,N)  # Generate point
    sigma = np.random.random()  # Generate sigma number [0,1]

    f.write(str(p) + "\t" + str(sigma) + "\n")  # Save data on file .txt

    i += 1
