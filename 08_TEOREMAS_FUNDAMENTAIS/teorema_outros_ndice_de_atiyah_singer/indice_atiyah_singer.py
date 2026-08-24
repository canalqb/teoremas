# nome do script: indice_atiyah_singer.py

import numpy as np
import pandas as pd

# Definir os dados da tabela inicial
dados = {
    'N': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Inicio (2^N)': [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],
    'Fim (2^(N+1))-1': [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Função para calcular o valor esperado pelo teorema (aproximadamente)
def calcular_indice_atiyah_singer(inicio, fim):
    # Aqui, você pode aplicar alguma fórmula ou aproximação baseada no teorema.
    # Para fins ilustrativos, vamos usar uma fórmula simples para aproximar os valores esperados.
    
    # Aprox. uma média aritmética no intervalo para os valores esperados.
    return (inicio + fim) // 2  # Média simples para o valor esperado

# Aplicar a função para calcular a coluna "Esperado pelo teorema"
df['Esperado pelo teorema'] = df.apply(lambda row: calcular_indice_atiyah_singer(row['Inicio (2^N)'], row['Fim (2^(N+1))-1']), axis=1)

# Exibir a tabela final
print(df)

# Salvar os resultados em um arquivo CSV, caso deseje analisar fora do script
df.to_csv('indice_atiyah_singer_resultados.csv', index=False)
