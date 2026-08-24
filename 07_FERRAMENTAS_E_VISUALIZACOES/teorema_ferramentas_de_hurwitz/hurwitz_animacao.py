import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Potências de 2 e Mersenne
n_values = range(1, 6)  # menos curvas para facilitar visualização
powers_of_two = [2**n for n in n_values]
mersennes = [p - 1 for p in powers_of_two]

# 2. Domínio
z0 = 0
z_left = -10
z_right = 10

# 3. Definição da função
def f_n(z, M_n):
    return np.sin(z / M_n)

# 4. Imprimir tabela
print("Tabela de dados:")
print(f"{'n':^3} | {'2^n':^5} | {'Mersenne (2^n - 1)':^20} | {'f_n(0)':^10} | {'f_n(-10)':^10} | {'f_n(10)':^10}")
print("-" * 70)

for n, p, m in zip(n_values, powers_of_two, mersennes):
    f_center = f_n(z0, m)
    f_left = f_n(z_left, m)
    f_right = f_n(z_right, m)
    print(f"{n:^3} | {p:^5} | {m:^20} | {f_center:^10.4f} | {f_left:^10.4f} | {f_right:^10.4f}")

# 5. Preparar dados para animação
z = np.linspace(-10, 10, 500)
curves = [f_n(z, M_n) for M_n in mersennes]

# 6. Plot setup
fig, ax = plt.subplots(figsize=(8, 8))
lines = []
colors = plt.cm.viridis(np.linspace(0, 1, len(curves)))

for i in range(len(curves)):
    line, = ax.plot([], [], color=colors[i], label=f'f{i+1}(z)', linewidth=2)
    lines.append(line)

ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_title("Curvas $f_n(z) = \\sin(z / M_n)$ girando em círculos")
ax.legend()
ax.grid(True)
ax.set_aspect('equal')

# 7. Função de rotação
def rotate(x, y, angle_rad):
    cos_theta = np.cos(angle_rad)
    sin_theta = np.sin(angle_rad)
    x_rot = cos_theta * x - sin_theta * y
    y_rot = sin_theta * x + cos_theta * y
    return x_rot, y_rot

# 8. Função de animação
def animate(frame):
    for i, (line, y_vals) in enumerate(zip(lines, curves)):
        angle = 0.02 * frame * (i + 1)
        x_rot, y_rot = rotate(z, y_vals, angle)
        line.set_data(x_rot, y_rot)
    return lines

# 9. Criar animação
anim = FuncAnimation(fig, animate, frames=300, interval=30, blit=True)

# 10. Exibir o gráfico
plt.show()

# anim.save('curvas_rotacionando.gif', writer='pillow', fps=30)
anim.save('curvas_rotacionando.gif', writer='pillow', fps=30)
