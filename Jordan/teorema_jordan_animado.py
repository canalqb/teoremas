import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

# --- Dados baseados em potências de 2 e números de Mersenne ---
n = np.arange(2, 21)[::-1]  # n de 20 até 2, invertido
mersennes = 2**n - 1
base = np.log2(mersennes)
onda = 0.5 * np.sin(0.8 * n)  # Oscilação senoidal (curvas)
f = base + onda              # Função final com curvas

# --- Decomposição de f em f1 e f2 (funções crescentes) ---
f1 = np.zeros_like(f)
f2 = np.zeros_like(f)

for i in range(1, len(n)):
    f1[i] = f1[i-1] + abs(f[i] - f[i-1])
    f2[i] = f1[i] - f[i]

f_reconstructed = f1 - f2

# --- Tabela com todos os valores ---
df = pd.DataFrame({
    'n': n,
    'f(n) = base + onda': np.round(f, 4),
    'f1(n)': np.round(f1, 4),
    'f2(n)': np.round(f2, 4),
    'f1(n) - f2(n)': np.round(f_reconstructed, 4)
})

print("\nTabela de valores usados para os gráficos:\n")
print(df.to_string(index=False))

# --- Configurações para animação estilo "onda na água" ---
amp = 0.3         # Amplitude da onda
decay = 0.1       # Decaimento da onda
speed = 0.3       # Velocidade da onda
pos_pedra = len(n)//2  # Posição da "pedra"
frames = 60       # Total de frames da animação

# --- Criar 4 gráficos (f, f1, f2, f1-f2) ---
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
axs = axs.flatten()

dados = [f, f1, f2, f_reconstructed]
titulos = [
    'Função com base em Mersenne + onda senoidal (f)',
    'Função crescente f1(n)',
    'Função crescente f2(n)',
    'Verificação: f1(n) - f2(n)'
]
cores = ['blue', 'green', 'orange', 'red']
legendas = [
    'f(n) = base + onda',
    'f1(n) (crescente)',
    'f2(n) (crescente)',
    'f1(n) - f2(n)'
]

lines = []
annotations = []

# --- Criar linhas e anotações nos gráficos ---
for i, ax in enumerate(axs):
    line, = ax.plot(n, dados[i], 'o-', color=cores[i], label=legendas[i])
    ax.set_title(titulos[i])
    ax.grid(True)
    ax.legend()
    
    # Anotações dos pontos
    anns = []
    for (xi, yi) in zip(n, dados[i]):
        ann = ax.annotate(f"{yi:.2f}", (xi, yi), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)
        anns.append(ann)
    
    lines.append(line)
    annotations.append(anns)

plt.tight_layout()

# --- Função de atualização para animação ---
def update(frame):
    for i, line in enumerate(lines):
        y_original = np.copy(dados[i])
        dist = np.abs(np.arange(len(n)) - pos_pedra)
        perturb = amp * np.sin(2 * np.pi * (dist - speed * frame) / 3) * np.exp(-decay * dist)
        y_anim = y_original + perturb
        
        line.set_ydata(y_anim)
        
        # Atualiza anotações
        for ann, xi, yi in zip(annotations[i], n, y_anim):
            ann.xy = (xi, yi)
            ann.set_text(f"{yi:.2f}")
    
    return lines + [ann for sublist in annotations for ann in sublist]

# --- Criar animação ---
anim = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# --- Mostrar animação ---
plt.show()

# --- Salvar animação como GIF ---
gif_path = "animacao_teorema_jordan.gif"
anim.save(gif_path, writer='pillow', fps=20)
print(f"\n✅ GIF salvo com sucesso em: {gif_path}")
