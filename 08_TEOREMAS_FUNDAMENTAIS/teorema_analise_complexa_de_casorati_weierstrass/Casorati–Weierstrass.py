import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(z):
    return np.exp(1 / z)

# Pontos: potências de 2 e Mersennes
powers_of_two = np.array([2**n for n in range(11)], dtype=complex)
primes = [2, 3, 5, 7, 11]
mersennes = np.array([2**p - 1 for p in primes], dtype=complex)
z_points = np.concatenate((powers_of_two, mersennes))
fz_points = f(z_points)

# Separar potências de 2 e mersennes para cores
fz_powers = fz_points[:len(powers_of_two)]
fz_mersennes = fz_points[len(powers_of_two):]

# Centralizar e escalar para visualização
min_index = np.argmin(np.abs(fz_points))
min_point = fz_points[min_index]
fz_points_centered = fz_points - min_point
max_dist = np.max(np.abs(fz_points_centered))
scale = 1 / max_dist
fz_points_scaled = fz_points_centered * scale
fz_powers_scaled = fz_points_scaled[:len(powers_of_two)]
fz_mersennes_scaled = fz_points_scaled[len(powers_of_two):]

# Definir velocidades angulares diferentes (rad/frame)
num_points = len(fz_points_scaled)
velocities_deg = np.random.uniform(0.5, 2.0, num_points)
velocities = np.deg2rad(velocities_deg)
velocities_powers = velocities[:len(powers_of_two)]
velocities_mersennes = velocities[len(powers_of_two):]

# Imprimir tabela de valores
print("Tabela de valores dos pontos:")
print(f"{'Index':>5} | {'Tipo':>12} | {'z (input)':>20} | {'f(z) (output)':>25} | {'Velocidade (°/frame)':>20}")
print("-" * 95)
for i, (z, fz_val, vel_deg) in enumerate(zip(z_points, fz_points, velocities_deg)):
    tipo = "Potência de 2" if i < len(powers_of_two) else "Número de Mersenne"
    print(f"{i:5d} | {tipo:12} | {str(z):>20} | {str(fz_val):>25} | {vel_deg:20.3f}")

# Plot
fig, ax = plt.subplots(figsize=(8, 8))
scat_powers = ax.scatter(fz_powers_scaled.real, fz_powers_scaled.imag, s=100, alpha=0.8, color='blue', label='Potências de 2')
scat_mersennes = ax.scatter(fz_mersennes_scaled.real, fz_mersennes_scaled.imag, s=100, alpha=0.8, color='orange', label='Números de Mersenne')

ax.set_title(r'Valores de $f(z) = e^{1/z}$ em potências de 2 e números de Mersenne (velocidades diferentes)')
ax.set_xlabel('Re$(f(z))$')
ax.set_ylabel('Im$(f(z))$')
ax.grid(True)
ax.axis('equal')
lim = 1.2
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.legend()

def update(frame):
    angles_powers = velocities_powers * frame
    angles_mersennes = velocities_mersennes * frame

    rotated_powers = fz_powers_scaled * np.exp(1j * angles_powers)
    rotated_mersennes = fz_mersennes_scaled * np.exp(1j * angles_mersennes)

    scat_powers.set_offsets(np.c_[rotated_powers.real, rotated_powers.imag])
    scat_mersennes.set_offsets(np.c_[rotated_mersennes.real, rotated_mersennes.imag])

    return scat_powers, scat_mersennes

ani = FuncAnimation(fig, update, frames=np.arange(0, 360*3, 2), interval=50, blit=True, repeat=True)

plt.show()
