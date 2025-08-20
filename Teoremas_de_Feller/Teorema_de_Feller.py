import pandas as pd

# Define os IDs de 0 até 16
ids = list(range(0, 17))

# Calcula início, fim e meio conforme a fórmula
tabela = []
for ID in ids:
    inicio = 2**ID
    fim = 2**(ID + 1) - 1
    meio = (inicio + fim) // 2  # ou: (3 * 2**ID - 1) // 2
    tabela.append((inicio, meio, fim))

# Cria DataFrame
df = pd.DataFrame(tabela, columns=['Início (2^ID)', 'Meio', 'Fim (2^(ID+1)-1)'])

# Exibe
print(df.to_string(index=False))


import pandas as pd

# Valores dados manualmente
dados = [
    (1, 1, 1),
    (2, 3, 3),
    (4, 7, 7),
    (8, 8, 15),
    (16, 21, 31),
    (32, 49, 63),
    (64, 76, 127),
    (128, 224, 255),
    (256, 467, 511),
    (512, 514, 1023),
    (1024, 1155, 2047),
    (2048, 2683, 4095),
    (4096, 5216, 8191),
    (8192, 10544, 16383),
    (16384, 26867, 32767),
    (32768, 51510, 65535),
    (65536, 95823, 131071)
]

# Criação do DataFrame
df = pd.DataFrame(dados, columns=['Início (2^ID)', 'Meio (ajustado)', 'Fim (2^(ID+1)-1)'])

# Cálculo da média teórica para comparação
df['Média Teórica'] = (df['Início (2^ID)'] + (df['Início (2^ID)']*2)) // 2
df['Desvio'] = df['Meio (ajustado)'] - df['Média Teórica']

# Exibição da tabela completa
print(df.to_string(index=False))
