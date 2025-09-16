import sympy as sp
from sympy import symbols, exp

def gerar_mersenne(primos):
    return [2**p - 1 for p in primos]

def testar_identidade_em_pontos(f, g, pontos):
    resultados = []
    for x_val in pontos:
        f_val = f.subs(z, x_val).evalf()
        g_val = g.subs(z, x_val).evalf()
        iguais = sp.simplify(f_val - g_val) == 0
        resultados.append((x_val, f_val, g_val, iguais))
    return resultados

# Definir variável simbólica
z = symbols('z')

# Definir duas funções analíticas (exemplo)
f = exp(z)  # f(z) = e^z
g = exp(z)  # g(z) = e^z (igual, para teste)

# Gerar pontos - potências de 2 e números de Mersenne para p = 2,3,5,7
potencias_de_2 = [2**n for n in range(6)]  # 1,2,4,8,16,32
primos = [2,3,5,7]
mersennes = gerar_mersenne(primos)

pontos_teste = potencias_de_2 + mersennes

# Testar identidade em todos esses pontos
resultados = testar_identidade_em_pontos(f, g, pontos_teste)

# Mostrar resultados
print("Ponto\tf(z)\tg(z)\tIgual?")
for (p, fv, gv, igual) in resultados:
    print(f"{p}\t{fv:.5f}\t{gv:.5f}\t{igual}")

print("\nSe as funções coincidirem nesses pontos e as funções forem analíticas,\n" \
      "pela unicidade da série de Taylor, as funções são idênticas em todo domínio onde são analíticas.")
