# teorema_whitney.py
import numpy as np

# Definindo os valores da tabela
dados_tabela = [
    (0, 1, 1, 1),
    (1, 2, 3, 3),
    (2, 4, 7, 7),
    (3, 8, 8, 15),
    (4, 16, 21, 31),
    (5, 32, 49, 63),
    (6, 64, 76, 127),
    (7, 128, 224, 255),
    (8, 256, 467, 511),
    (9, 512, 514, 1023)
]

# Função que calcula o valor esperado com base no teorema (usando a tabela)
def valor_esperado(teorema_tabela, N):
    inicio = teorema_tabela[N][1]
    fim = teorema_tabela[N][3]
    
    # Fazendo uma interpolação linear simples entre "Inicio" e "Fim"
    valor_esperado = (inicio + fim) / 2
    return valor_esperado

# Gerando a tabela e calculando os valores esperados
tabela_resultados = []
for N in range(10):
    valor_esperado_teorema = valor_esperado(dados_tabela, N)
    tabela_resultados.append((N, dados_tabela[N][1], valor_esperado_teorema, dados_tabela[N][3]))

# Imprimindo a tabela com os resultados
print("N  | Inicio (2^N) | Esperado pelo Teorema | Fim (2^(N+1))-1")
for linha in tabela_resultados:
    print(f"{linha[0]}  | {linha[1]}           | {linha[2]:.0f}                | {linha[3]}")
