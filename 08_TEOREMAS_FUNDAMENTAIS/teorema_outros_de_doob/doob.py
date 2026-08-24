import numpy as np

np.random.seed(123)

# Parâmetros
N = 1000  # número de passos do martingale
M = 500   # número de simulações para estimar médias condicionais

# Simula incrementos ±1 com prob 0.5
increments = np.random.choice([-1, 1], size=(M, N))

# Soma acumulada para cada simulação = martingale
martingales = np.cumsum(increments, axis=1)

# Tempo presente (t)
t = 500

# Tempo futuro (T), T > t
T = 700

# Valor do martingale no tempo t para cada simulação
Mt = martingales[:, t-1]

# Valor do martingale no tempo T para cada simulação
MT = martingales[:, T-1]

# Agora, queremos estimar E[MT | informação até tempo t]
# Em um martingale, essa esperança condicional deve ser igual a Mt

# Como não temos a informação "real" do passado (filtração),
# vamos fazer uma aproximação simples agrupando as simulações com valor Mt semelhante

# Criar "bins" para agrupar valores próximos de Mt
bins = np.arange(Mt.min(), Mt.max() + 2)  # +2 para incluir o último bin
indices = np.digitize(Mt, bins)

# Para cada bin, calcular média de MT e média de Mt
import collections
bin_MT_means = collections.defaultdict(list)
bin_Mt_means = collections.defaultdict(list)

for idx, mt_val, mt_val_T in zip(indices, Mt, MT):
    bin_MT_means[idx].append(mt_val_T)
    bin_Mt_means[idx].append(mt_val)

print(f"{'Bin Mt':>8} {'Média Mt':>10} {'Média MT':>10} {'Diferença':>10}")
print("-" * 42)
for b in sorted(bin_MT_means.keys()):
    mean_Mt = np.mean(bin_Mt_means[b])
    mean_MT = np.mean(bin_MT_means[b])
    diff = abs(mean_MT - mean_Mt)
    print(f"{b:8} {mean_Mt:10.2f} {mean_MT:10.2f} {diff:10.4f}")

print("\nObservação:")
print("A média de MT condicional ao valor de Mt é aproximadamente igual a Mt,")
print("demonstrando a propriedade do martingale prevista pelo Teorema de Doob.")
