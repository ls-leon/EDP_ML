import numpy as np
import matplotlib.pyplot as plt

# Paramètres
Nx = 50  # nb de points en espace
Nt = 100  # nb de points en temps
L = 1.0  # longueur du domaine
T = 0.1  # temps final
alpha = 0.01  # diffusivité thermique

h = L / (Nx - 1)
dt = T / (Nt - 1)
lmbda = alpha * dt / h**2

x = np.linspace(0, L, Nx)
u = np.zeros((Nt, Nx))

def initial_condition(x):
    return np.sin(np.pi * x)

u[0, :] = initial_condition(x)

for n in range(Nt - 1):
    for i in range(1, Nx - 1):
        u[n+1, i] = u[n, i] + lmbda * (u[n, i+1] - 2*u[n, i] + u[n, i-1])

# Affichage de la température à t = T/2
plt.plot(x, u[Nt//2, :], label='t = T/2', color = 'red')

plt.xlabel('Position x')
plt.ylabel('Température u(x, t)')
plt.title('Température à t = T/2')
plt.legend()
plt.grid(True)
plt.show()
