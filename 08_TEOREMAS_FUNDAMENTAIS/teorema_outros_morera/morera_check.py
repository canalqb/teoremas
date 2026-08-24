import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f_potencias(z, N=9):
    return sum((2**n) * (z**n) for n in range(N+1))

def mersenne(n):
    return 2**n - 1

def f_mersenne(z, N=10):
    val = 0
    for i in range(N+1):
        k = i // 2
        if i % 2 == 0:
            coef = mersenne(k) if k > 0 else 0
        else:
            coef = mersenne(k)/2 if k > 0 else 0
        val += coef * (z**i)
    return val

# Triângulo base no centro (0,0), (1,0), (0,1)
tri_base = np.array([0+0j, 1+0j, 0+1j])

fig, ax = plt.subplots(figsize=(8,6))

# Grade para o módulo
x = np.linspace(-2, 2, 400)
y = np.linspace(-1.5, 2, 400)
X, Y = np.meshgrid(x, y)
Z = X + 1j*Y

# Para animar
frames = 60

line_pot, = ax.plot([], [], 'r-', lw=3, label='Potências de 2')
line_mer, = ax.plot([], [], 'b-', lw=3, label='Mersennes')

contour_pot = None
contour_mer = None

def init():
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 2)
    ax.set_xlabel('Re(z)')
    ax.set_ylabel('Im(z)')
    ax.set_title('Animação dos triângulos movendo-se para o centro')
    ax.grid(True)
    ax.legend()
    return line_pot, line_mer

def update(frame):
    # Remove contornos antigos
    for coll in ax.collections:
        coll.remove()

    t = frame / (frames - 1)

    desloc_pot = -2 * (1 - t)
    tri_pot = tri_base + desloc_pot

    desloc_mer = 2 * (1 - t)
    tri_mer = tri_base + desloc_mer

    line_pot.set_data(np.append(tri_pot.real, tri_pot[0].real),
                      np.append(tri_pot.imag, tri_pot[0].imag))
    line_mer.set_data(np.append(tri_mer.real, tri_mer[0].real),
                      np.append(tri_mer.imag, tri_mer[0].imag))

    Z_pot = Z - desloc_pot
    F_pot = np.abs(f_potencias(Z_pot))
    ax.contour(X, Y, F_pot, levels=30, cmap='Reds', alpha=0.6)

    Z_mer = Z - desloc_mer
    F_mer = np.abs(f_mersenne(Z_mer))
    ax.contour(X, Y, F_mer, levels=30, cmap='Blues', alpha=0.6)

    return line_pot, line_mer



anim = FuncAnimation(fig, update, frames=frames, init_func=init, blit=False, interval=50)

anim.save('morera_animation.gif', writer='pillow', fps=20)
plt.show()
