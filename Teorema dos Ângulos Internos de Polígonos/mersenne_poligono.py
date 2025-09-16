def soma_angulos_internos_mersenne(p):
    # Calcula o número de Mersenne
    n = 2**p - 1
    
    # Calcula a soma dos ângulos internos usando o teorema
    soma_angulo = (n - 2) * 180
    
    return n, soma_angulo

def main():
    print("Cálculo da soma dos ângulos internos para polígono com lados de número de Mersenne")
    p = int(input("Digite um número primo p: "))
    
    # Aqui poderia ter uma verificação se p é primo, mas para simplificar vamos assumir que sim
    
    n, soma = soma_angulos_internos_mersenne(p)
    print(f"\nNúmero de lados (Mersenne): n = 2^{p} - 1 = {n}")
    print(f"Soma dos ângulos internos do polígono: (n - 2) x 180° = {soma}°")

if __name__ == "__main__":
    main()
