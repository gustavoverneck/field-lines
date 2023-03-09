import numpy as np
import matplotlib.pyplot as plt

## Dada uma carga q na origem (0,0)

def E(x, y):
    q = 0.1 # C
    k = 8.99 * 10E9
    return q/(x**2 + y**2)*x, q/(x**2 + y**2)*y

x, y = np.meshgrid(np.linspace(-10, 10, 10), np.linspace(-10, 10, 10))

u, v = E(x, y)
fig, ax = plt.subplots()
# Plotting Vector Field with QUIVER
#plt.quiver(x, y, u, v, color='g')
plt.streamplot(x, y, u, v, color='g')
plt.title('Campo Elétrico')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.plot(0, 0, 'or')

# Setting x, y boundary limits
plt.xlim(-10, 10)
plt.ylim(-10, 10)
  
# Show plot with grid
plt.grid()
plt.savefig("campo-eletrico-stream.png")
plt.show()