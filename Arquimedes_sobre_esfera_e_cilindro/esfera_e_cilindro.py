import numpy as np
import matplotlib.pyplot as plt

def calcular_valores(r):
    vol_esfera = (4/3) * np.pi * r**3
    vol_cilindro = 2 * np.pi * r**3
    area_esfera = 4 * np.pi * r**2
    area_cilindro = 6 * np.pi * r**2
    rel_vol = vol_esfera / vol_cilindro if vol_cilindro != 0 else np.nan
    rel_area = area_esfera / area_cilindro if area_cilindro != 0 else np.nan
    return vol_esfera, vol_cilindro, rel_vol, area_esfera, area_cilindro, rel_area

def plot_esfera_cilindro(ax, r, titulo):
    h = 2 * r

    # Cilindro
    z_cil = np.linspace(-r, r, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    theta_grid, z_grid = np.meshgrid(theta, z_cil)
    x_cil = r * np.cos(theta_grid)
    y_cil = r * np.sin(theta_grid)
    ax.plot_surface(x_cil, y_cil, z_grid, alpha=0.3, color='blue')

    # Esfera
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x_sph = r * np.outer(np.cos(u), np.sin(v))
    y_sph = r * np.outer(np.sin(u), np.sin(v))
    z_sph = r * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x_sph, y_sph, z_sph, color='red', alpha=0.6)

    ax.set_title(titulo, fontsize=12)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_box_aspect([1,1,1])
    ax.view_init(elev=20, azim=30)

def plot_comparacao(n):
    raio_potencia = 2 ** n
    raio_mersenne = 2 ** n - 1

    # Calcular valores
    vals_pot = calcular_valores(raio_potencia)
    vals_mer = calcular_valores(raio_mersenne)

    # Imprimir tabela sem notação científica
    print(f"\n--- n = {n} ---")
    print(f"{'Raio':>6} | {'Vol Esfera':>12} | {'Vol Cilindro':>14} | {'Relação Vol':>11} | {'Área Esfera':>12} | {'Área Cilindro':>14} | {'Relação Área':>11}")
    print("-"*90)
    print(f"{raio_potencia:6} | {vals_pot[0]:12.2f} | {vals_pot[1]:14.2f} | {vals_pot[2]:11.4f} | {vals_pot[3]:12.2f} | {vals_pot[4]:14.2f} | {vals_pot[5]:11.4f}")
    print(f"{raio_mersenne:6} | {vals_mer[0]:12.2f} | {vals_mer[1]:14.2f} | {vals_mer[2]:11.4f} | {vals_mer[3]:12.2f} | {vals_mer[4]:14.2f} | {vals_mer[5]:11.4f}")

    # Plot
    fig = plt.figure(figsize=(14, 6))

    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    plot_esfera_cilindro(ax1, raio_potencia, f"Raio = 2^{n} = {raio_potencia}")

    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    plot_esfera_cilindro(ax2, raio_mersenne, f"Raio = 2^{n} - 1 = {raio_mersenne} (Mersenne)")

    plt.suptitle(f"Comparação para n = {n}", fontsize=14)
    plt.tight_layout()
    plt.show()

# Exemplo para múltiplos valores de n
for n in range(1, 6):
    plot_comparacao(n)
