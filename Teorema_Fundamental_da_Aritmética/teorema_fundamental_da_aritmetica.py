from sympy import factorint

# Números a destacar
destaques = {1, 3, 7, 8, 21, 49, 76}

# Número de intervalos
for i in range(5):
    start = 2**i
    end = 2**(i+1) - 1
    print(f"\nIntervalo [{start}, {end}]:")
    print("-" * 30)

    for n in range(start, end + 1):
        factors = factorint(n)  # retorna {primo: expoente}
        factor_str = " * ".join([f"{p}^{e}" if e > 1 else f"{p}" for p, e in factors.items()])
        
        if n in destaques:
            print(f">>>>> {n} = {factor_str} <<<<<")  # Destaque visual
        else:
            print(f"{n} = {factor_str}")
 
