import numpy as np
import matplotlib.pyplot as plt

## Dada uma carga q na origem (0,0)

def E(x, y):
    #q1 = 1 # C
    #q2 = -1
    #k = 1.0
    #d = 1.0
    #pos1 = np.array([-d, 0])
    #pos2 = np.array([d, 0])
    Ex = (x + 1) / ((x+1)**2 + y**2) - (x - 1) / ((x-1)**2 + y**2)
    Ey = y / ((x+1)**2 + y**2) - y/((x-1)**2 + y**2) 
    return Ex, Ey


x = np.arange(-4, 4, 0.01)
y = np.arange(-4, 4, 0.01)
x, y = np.meshgrid(x, y)
u, v = E(x, y)


fig, ax = plt.subplots()
ax.set_aspect('equal')
# Plotting Vector Field with QUIVER
#plt.quiver(x, y, u, v, color='g')  # Quiver nao funciona bem
ax.streamplot(x, y, u, v)
plt.title('Campo Elétrico - Dipolo Eletrico')
ax.plot(-1, 0, '-or')
ax.plot(+1, 0, 'ob')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Setting x, y boundary limits
plt.xlim(-4, 4)
plt.ylim(-4, 4)
  
# Show plot with grid
plt.grid()
plt.savefig("dipolo-eletrico-quiver.png")
plt.show()