import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x, y):
    return x**2 * y + np.sin(x*y)

def dfdxdy(x, y, h=1e-5):
    return ( (f(x + h, y + h) - f(x + h, y)) - (f(x, y + h) - f(x, y)) ) / (h**2)

def dfdy_dx(x, y, h=1e-5):
    return ( (f(x + h, y + h) - f(x, y + h)) - (f(x + h, y) - f(x, y)) ) / (h**2)

exps = np.arange(-2, 3, dtype=float)
vals = 2.0 ** exps

x_vals = np.linspace(min(vals)*0.8, max(vals)*1.2, 50)
y_vals = np.linspace(min(vals)*0.8, max(vals)*1.2, 50)
X, Y = np.meshgrid(x_vals, y_vals)

diff = np.zeros_like(X, dtype=float)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        val1 = dfdxdy(X[i, j], Y[i, j])
        val2 = dfdy_dx(X[i, j], Y[i, j])
        diff[i, j] = val1 - val2

x_min, x_max = min(vals)*0.8, max(vals)*1.2
y_min, y_max = min(vals)*0.8, max(vals)*1.2
z_plane = np.min(diff) - 0.1

hor_y = vals
ver_x = vals

offset = 1.5

def random_outside():
    side = np.random.choice(['left', 'right', 'bottom', 'top'])
    if side == 'left':
        x = x_min - offset*(x_max - x_min)*np.random.rand()
        y = np.random.uniform(y_min, y_max)
    elif side == 'right':
        x = x_max + offset*(x_max - x_min)*np.random.rand()
        y = np.random.uniform(y_min, y_max)
    elif side == 'bottom':
        x = np.random.uniform(x_min, x_max)
        y = y_min - offset*(y_max - y_min)*np.random.rand()
    else:
        x = np.random.uniform(x_min, x_max)
        y = y_max + offset*(y_max - y_min)*np.random.rand()
    return x, y

hor_lines_start = []
for y in hor_y:
    x0, y0 = random_outside()
    hor_lines_start.append({'x_start': x0, 'x_end': x0, 'y': y0})

ver_lines_start = []
for x in ver_x:
    x0, y0 = random_outside()
    ver_lines_start.append({'x': x0, 'y_start': y0, 'y_end': y0})

# --- Novos parâmetros para animação ---

fps = 60                 # frames por segundo (mais suave)
duration_move = 1        # segundos da animação de movimento
duration_pause = 10      # segundos de pausa na imagem final

frames_move = fps * duration_move
frames_pause = fps * duration_pause
total_frames = frames_move + frames_pause

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Diferença')
ax.set_title('Diferença entre derivadas mistas com linhas animadas')

ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_zlim(np.min(diff)-0.2, np.max(diff)+0.2)

def lerp(start, end, t):
    return start + (end - start)*t

def animate(frame):
    ax.clear()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_zlim(np.min(diff)-0.2, np.max(diff)+0.2)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('Diferença')
    ax.set_title('Diferença entre derivadas mistas com linhas animadas')

    # Desenha a superfície fixa
    ax.plot_surface(X, Y, diff, cmap='viridis', alpha=0.7)

    # Determina progresso apenas se estiver na fase de movimento
    if frame < frames_move:
        t = frame / frames_move
    else:
        t = 1  # mantém final durante pausa

    # Linhas horizontais
    for i, y_target in enumerate(hor_y):
        start = hor_lines_start[i]
        y = lerp(start['y'], y_target, t)
        x_start_final = x_min
        x_end_final = x_max
        half_length = (x_end_final - x_start_final) / 2
        center = lerp(start['x_start'], (x_start_final + x_end_final)/2, t)
        length = lerp(0, half_length, t)
        x_start = center - length
        x_end = center + length
        ax.plot([x_start, x_end], [y, y], [z_plane]*2, color='black', lw=2)

    # Linhas verticais
    for i, x_target in enumerate(ver_x):
        start = ver_lines_start[i]
        x = lerp(start['x'], x_target, t)
        y_start_final = y_min
        y_end_final = y_max
        half_length = (y_end_final - y_start_final) / 2
        center = lerp(start['y_start'], (y_start_final + y_end_final)/2, t)
        length = lerp(0, half_length, t)
        y_start = center - length
        y_end = center + length
        ax.plot([x, x], [y_start, y_end], [z_plane]*2, color='black', lw=2)

    return []

ani = animation.FuncAnimation(fig, animate, frames=total_frames, interval=1000/fps, blit=False)

plt.show()
