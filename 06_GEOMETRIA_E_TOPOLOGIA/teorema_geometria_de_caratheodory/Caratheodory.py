import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Gerar números de Mersenne 2^(n+1)-1 para n=0..10
n_values = np.arange(0, 11)
mersenne = 2**(n_values + 1) - 1

points = np.vstack((mersenne % 20, (mersenne * 2) % 20, (mersenne * 3) % 20)).T
convex_point = np.mean(points, axis=0)

# Imprimir tabela de valores
print("Tabela de pontos Mersenne (x, y, z):")
print("-" * 35)
print(f"{'Index':>5} | {'X':>5} | {'Y':>5} | {'Z':>5}")
print("-" * 35)
for i, (x, y, z) in enumerate(points):
    print(f"{i:5} | {x:5} | {y:5} | {z:5}")
print("-" * 35)
print(f"Ponto convexo (média dos pontos): ({convex_point[0]:.2f}, {convex_point[1]:.2f}, {convex_point[2]:.2f})")
print()

# Setup do plot
fig = plt.figure(figsize=(6, 10), facecolor='none')  # fundo transparente
ax = fig.add_subplot(111, projection='3d', facecolor='none')

ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_zlim(0, 20)

fps = 30
total_frames = 15 * fps
delay_between_points = int(0.1 * fps)  # 0.1 segundos entre pontos

def update(frame):
    ax.clear()
    ax.set_facecolor((0,0,0,0))  # fundo transparente no eixo também
    
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)
    ax.set_zlim(0, 20)
    
    # REMOVER planos, grades e ticks
    ax.grid(False)
    ax.xaxis.line.set_color((0,0,0,0))
    ax.yaxis.line.set_color((0,0,0,0))
    ax.zaxis.line.set_color((0,0,0,0))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_box_aspect([1, 10/6, 1])  # aspecto 9:16 (6x10 approx)

    # Título e labels removidos para "base zero"
    # ax.set_title("Teorema de Carathéodory: combinação convexa em 3D")
    # ax.set_xlabel("X")
    # ax.set_ylabel("Y")
    # ax.set_zlabel("Z")

    points_to_show = min(len(points), frame // delay_between_points + 1)
    visible_points = points[:points_to_show]

    # Plotar pontos azuis
    pnts = ax.scatter(visible_points[:, 0], visible_points[:, 1], visible_points[:, 2],
                      color='blue', s=50, label='Pontos Mersenne')

    # Legendas ao lado dos pontos
    for i in range(points_to_show):
        x, y, z = points[i]
        ax.text(x, y, z, f"({x},{y},{z})", color='black', fontsize=8)

    # Ponto convexo vermelho
    pnt_convex = ax.scatter(convex_point[0], convex_point[1], convex_point[2],
                           color='red', s=100, label='Ponto Convexo')
    ax.text(convex_point[0], convex_point[1], convex_point[2], 
            f"({convex_point[0]:.1f},{convex_point[1]:.1f},{convex_point[2]:.1f})", 
            color='red', fontsize=10)

    # Linhas verdes ligando o ponto convexo aos pontos visíveis
    for i in range(points_to_show):
        ax.plot([convex_point[0], points[i, 0]],
                [convex_point[1], points[i, 1]],
                [convex_point[2], points[i, 2]], color='green', alpha=0.6, label='_nolegend_')

    # Legenda manual (pode tirar se quiser, pois sem base fica estranho)
    # handles = [pnts, pnt_convex]
    # labels = [h.get_label() for h in handles]
    # ax.legend(handles, labels, loc='upper left')

    # Texto explicativo final (removido para "clean")
    # if points_to_show == len(points):
    #     ax.text2D(0.05, 0.9,
    #               "Qualquer ponto no convexo pode ser representado\ncomo combinação de no máximo d+1 pontos (4 aqui).",
    #               transform=ax.transAxes)

    # Rotação "livre" (sem gravidade)
    az = 360 * (frame / total_frames) + 45 * np.sin(frame * 0.1)
    el = 30 * np.cos(frame * 0.05) + 30
    ax.view_init(elev=el, azim=az)

ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps)

# Salvar GIF
#ani.save("caratheodory_3d.gif", writer=PillowWriter(fps=fps))

print("GIF salvo como 'caratheodory_3d.gif' no diretório atual.")
