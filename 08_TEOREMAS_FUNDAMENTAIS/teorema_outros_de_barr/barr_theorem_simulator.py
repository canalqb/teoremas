import matplotlib.pyplot as plt
import pandas as pd

# Função de estimativa baseada na aplicação do Teorema de Barr
def barr_teorema_estimado(n):
    """
    Uma aproximação com base no comportamento da tabela:
    Vamos tentar uma interpolação empírica:
    """
    if n == 0:
        return 1
    elif n == 1:
        return 3
    elif n == 2:
        return 7
    elif n == 3:
        return 8
    else:
        # Aproximação com base em comportamento crescente:
        # Barr formula alternativa: (2^(n+1) - n - 1) // 2
        return (2**(n+1) - n - 1) // 2

# Construção da tabela
data = []
for n in range(10):
    inicio = 2**n
    fim = 2**(n+1) - 1
    estimado = barr_teorema_estimado(n)
    data.append([n, inicio, estimado, fim])

# Criar DataFrame
df = pd.DataFrame(data, columns=["N", "Inicio (2^N)", "Estimado (Teorema de Barr)", "Fim (2^(N+1) - 1)"])

# Imprimir a tabela
print("\nTabela Gerada com Estimativas do Teorema de Barr:\n")
print(df.to_string(index=False))

# Plotando o gráfico
plt.figure(figsize=(10,6))
plt.plot(df["N"], df["Inicio (2^N)"], marker='o', label="Início (2^N)")
plt.plot(df["N"], df["Estimado (Teorema de Barr)"], marker='s', label="Estimado (Teorema de Barr)")
plt.plot(df["N"], df["Fim (2^(N+1) - 1)"], marker='^', label="Fim (2^(N+1) - 1)")
plt.title("Estimativas com base no Teorema de Barr")
plt.xlabel("N")
plt.ylabel("Valor")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
