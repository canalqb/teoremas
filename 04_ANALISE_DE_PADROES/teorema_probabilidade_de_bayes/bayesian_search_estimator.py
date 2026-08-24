import numpy as np
import pandas as pd

# Dados originais da tabela (sem usar 'Procura' no cálculo)
data = {
    "Inicio": [1, 2, 4, 8, 16, 32, 64, 128],
    "Fim":    [2, 4, 8, 16, 32, 64, 128, 256]
}

df = pd.DataFrame(data)
df['Tamanho'] = df['Fim'] - df['Inicio']

# Prior proporcional ao tamanho do intervalo
total_tamanho = df['Tamanho'].sum()
df['P_H'] = df['Tamanho'] / total_tamanho

# Para estimar o "valor esperado da procura" em cada intervalo,
# vamos assumir que o valor está distribuído uniformemente no intervalo,
# e usar o centro do intervalo como estimativa do valor esperado

df['Procura_estimado'] = ((df['Inicio'] + df['Fim']) / 2).astype(int)

# Agora normalizamos a coluna estimada para aproximar o total de "Procura" observada
# Para comparação: o total esperado da "Procura" (com base no dado original)
total_procura_real = 1+3+7+8+21+49+76+224  # soma da coluna real (se quiser comparar)

# Escalar os valores estimados para que a soma seja igual ao total da procura real
soma_estimado = df['Procura_estimado'].sum()
df['Procura_estimado'] = (df['Procura_estimado'] / soma_estimado) * total_procura_real
df['Procura_estimado'] = df['Procura_estimado'].round().astype(int)

# Exibir a tabela comparativa
print("Comparação entre Procura real e Procura estimado pelo modelo simples:\n")
print(df[['Inicio', 'Fim', 'Procura_estimado']])
