def verificar_teorema_de_euler(v, a, f):
    resultado = v - a + f
    print(f"\nV - A + F = {v} - {a} + {f} = {resultado}")
    
    if resultado == 2:
        print("✅ O Teorema de Euler é satisfeito!")
    else:
        print("❌ O Teorema de Euler NÃO é satisfeito.")
        print("   Isso pode indicar que o poliedro não é convexo ou há um erro nos dados.")

# Entrada do usuário
try:
    print("=== Verificador do Teorema de Euler (Poliedros) ===")
    V = int(input("Digite o número de vértices (V): "))
    A = int(input("Digite o número de arestas (A): "))
    F = int(input("Digite o número de faces (F): "))

    verificar_teorema_de_euler(V, A, F)

except ValueError:
    print("Por favor, insira apenas números inteiros.")
