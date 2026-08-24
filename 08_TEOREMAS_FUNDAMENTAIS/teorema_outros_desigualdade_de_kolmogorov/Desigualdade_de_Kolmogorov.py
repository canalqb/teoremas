import pandas as pd

# Inicializar lista para armazenar os dados
dados = []

# Gerar valores para A de 0 a 8
for A in range(0, 9):
    n = 2 ** A
    lambda_val = 2 * n - 1  # 2^(A+1) - 1
    retorno_teorema = n / (lambda_val ** 2)  # Kolmogorov

    dados.append({
        '2^A': n,
        'Retorno do Teorema': round(retorno_teorema, 6),
        '2^(A+1) - 1': lambda_val
    })

# Criar DataFrame
tabela = pd.DataFrame(dados)

# Exibir
print(tabela.to_string(index=False))
