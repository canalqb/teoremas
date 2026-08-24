import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 1, 300)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1.05)
ax.set_zlim(0, 1.05)  # z agora vai ser valor normalizado entre 0 e 1 (posição relativa do expoente)

ax.set_xlabel("x")
ax.set_ylabel("f_k(x) = x^k")
ax.set_zlabel("Progresso da animação")

ax.set_title("Animação 3D suave com linhas chegando juntas")

n_min = 0
n_max = 7
num_lines = n_max - n_min + 1

colors = plt.cm.viridis(np.linspace(0, 1, num_lines))
linestyles = ['-', '--', '-.', ':'] * ((num_lines // 4) + 1)

lines = []
expoentes = []
start_exps = []
end_exps = []

for i, n in enumerate(range(n_min, n_max + 1)):
    start_exp = 2**n
    end_exp = 2**(n + 1) - 1
    expoentes.append(np.arange(start_exp, end_exp + 1))
    start_exps.append(start_exp)
    end_exps.append(end_exp)
    
    line, = ax.plot([], [], [], color=colors[i], linestyle=linestyles[i], lw=2, label=f"n={n}")
    lines.append(line)

ax.legend(loc='upper left')

total_frames = 360

def smooth_progress(t):
    # Função para suavizar o movimento (ease in/out)
    return 3*t**2 - 2*t**3  # Smoothstep

def init():
    for line in lines:
        line.set_data([], [])
        line.set_3d_properties([])
    return lines

def update(frame):
    t = frame / (total_frames - 1)
    
    elev = 30 + 20 * np.sin(np.radians(frame))  # rotação suave vertical
    azim = 45
    ax.view_init(elev=elev, azim=azim)
    
    for i, line in enumerate(lines):
        # Progresso suavizado para a linha i (vamos variar o tempo de animação para cada, para dar diferenciação)
        # Mas garantir que todas terminem em t=1
        t_i = smooth_progress(t ** (1 + i * 0.2))  # cada uma tem velocidade um pouco diferente
        
        # Interpolação do expoente entre start e end para tempo t_i
        k_float = start_exps[i] + t_i * (end_exps[i] - start_exps[i])
        
        # Como k_float não é inteiro, interpolamos potências (melhora suavidade)
        k_low = int(np.floor(k_float))
        k_high = min(int(np.ceil(k_float)), end_exps[i])
        alpha = k_float - k_low
        
        y_low = x ** k_low
        y_high = x ** k_high
        y = (1 - alpha) * y_low + alpha * y_high
        
        # z vai representar o progresso, vai de 0 a 1
        z = np.full_like(x, t_i)
        
        line.set_data(x, y)
        line.set_3d_properties(z)
    
    return lines

anim = FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=True, interval=50, repeat=True)

plt.show()
