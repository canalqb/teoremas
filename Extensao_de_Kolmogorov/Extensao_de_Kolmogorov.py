import numpy as np
import pandas as pd

# Criar a tabela original com base nas potências de 2
def construir_tabela(max_n=8):
    dados = []
    for n in range(max_n + 1):
        inicio = 2**n
        fim = (2**(n + 1)) - 1
        intervalo = list(range(inicio, fim + 1))
        ponto_procura = intervalo[len(intervalo) // 2]  # ponto médio do intervalo
        dados.append({
            "n": n,
            "Início": inicio,
            "Procura pelo teorema": ponto_procura,
            "Fim": fim,
            "Tamanho do intervalo": len(intervalo)
        })
    return pd.DataFrame(dados)

# Simular variáveis gaussianas independentes para cada intervalo
def simular_variaveis(df):
    simulacoes = []
    for _, row in df.iterrows():
        n = row["n"]
        indices = list(range(row["Início"], row["Fim"] + 1))
        valores = np.random.normal(loc=0, scale=1, size=len(indices))
        simulacoes.append((n, indices, valores))
    return simulacoes

# Execução
tabela_intervalos = construir_tabela(max_n=8)
simulacoes = simular_variaveis(tabela_intervalos)

# Exibir a tabela de intervalos
print(tabela_intervalos.to_string(index=False))
