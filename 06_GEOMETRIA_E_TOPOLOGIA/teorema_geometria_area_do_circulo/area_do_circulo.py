import math

print("n | 2^n | Mersenne (2^n - 1) | Área com raio 2^n | Área com raio Mersenne")
print("-" * 65)

for n in range(0, 11):
    pot_2 = 2 ** n
    mersenne = pot_2 - 1
    area_pot_2 = math.pi * (pot_2 ** 2)
    area_mersenne = math.pi * (mersenne ** 2)
    
    print(f"{n:2d} | {pot_2:4d} | {mersenne:17d} | {area_pot_2:16.2f} | {area_mersenne:19.2f}")
