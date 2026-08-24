import numpy as np
import matplotlib.pyplot as plt

# Operador linear contínuo e sobrejetivo
T = np.array([[2, 1],
              [1, 3]])

# Raio do círculo
radius = 1
k_max = 11

# Função para matriz de rotação de θ graus
def rotation_matrix(degrees):
    theta = np.radians(degrees)
    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

# Inicializa listas para armazenar todos os pontos rotacionados e transformados
pow2_points_rot = []
pow2_images = []
mersenne_points_rot = []
mersenne_images = []

print("k | 2^k | 2^(k+1)-1 | Rotação (°)")
print("-" * 35)

for k in range(k_max + 10):
    n_pow2 = 2**k
    n_mersenne = 2**(k + 1) - 1
    angle = k + 1  # graus de rotação

    print(f"{k:2d} | {n_pow2:4d} | {n_mersenne:10d} | {angle:3d}°")

    # Pontos da potência de 2
    theta_p = np.linspace(0, 2*np.pi, n_pow2, endpoint=False)
    x_p = radius * np.cos(theta_p)
    y_p = radius * np.sin(theta_p)
    pts_p = np.vstack((x_p, y_p))
    rot_p = rotation_matrix(angle) @ pts_p
    img_p = T @ rot_p
    pow2_points_rot.append(rot_p)
    pow2_images.append(img_p)

    # Pontos Mersenne
    theta_m = np.linspace(0, 2*np.pi, n_mersenne, endpoint=False)
    x_m = radius * np.cos(theta_m)
    y_m = radius * np.sin(theta_m)
    pts_m = np.vstack((x_m, y_m))
    rot_m = rotation_matrix(angle) @ pts_m
    img_m = T @ rot_m
    mersenne_points_rot.append(rot_m)
    mersenne_images.append(img_m)

# 🔷 Gráfico para Potências de 2
fig1, axs1 = plt.subplots(1, 2, figsize=(14, 6))
axs1[0].set_title("Potências de 2 – Domínio rotacionado")
axs1[1].set_title("Potências de 2 – Imagem sob T")

for pts, img in zip(pow2_points_rot, pow2_images):
    axs1[0].scatter(pts[0], pts[1], color='blue', alpha=0.2, s=5)
    axs1[1].scatter(img[0], img[1], color='red', alpha=0.2, s=5)

axs1[0].axis('equal')
axs1[1].axis('equal')
axs1[0].grid(True)
axs1[1].grid(True)

# 🔶 Gráfico para Mersenne
fig2, axs2 = plt.subplots(1, 2, figsize=(14, 6))
axs2[0].set_title("Mersenne – Domínio rotacionado")
axs2[1].set_title("Mersenne – Imagem sob T")

for pts, img in zip(mersenne_points_rot, mersenne_images):
    axs2[0].scatter(pts[0], pts[1], color='green', alpha=0.2, s=5)
    axs2[1].scatter(img[0], img[1], color='orange', alpha=0.2, s=5)

axs2[0].axis('equal')
axs2[1].axis('equal')
axs2[0].grid(True)
axs2[1].grid(True)

# Títulos gerais
fig1.suptitle("Visualização Sobreposta – Potências de 2 com Rotações Incrementais", fontsize=12)
fig2.suptitle("Visualização Sobreposta – Mersennes com Rotações Incrementais", fontsize=12)

plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.show()
