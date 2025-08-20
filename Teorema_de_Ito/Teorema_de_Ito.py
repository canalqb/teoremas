import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import plotly.express as px

# Dados fornecidos
dados = [
    (1, 1, 1), (2, 3, 3), (4, 7, 7), (8, 8, 15), (16, 21, 31), (32, 49, 63),
    (64, 76, 127), (128, 224, 255), (256, 467, 511), (512, 514, 1023),
    (1024, 1155, 2047), (2048, 2683, 4095), (4096, 5216, 8191),
    (8192, 10544, 16383), (16384, 26867, 32767), (32768, 51510, 65535)
]

# Separar as colunas
x = np.array([d[0] for d in dados])
y = np.array([d[1] for d in dados])
z = np.array([d[2] for d in dados])

# Modelo polinomial de grau 2
def modelo_polinomial(x, a, b, c):
    return a * x**2 + b * x + c

# Ajuste do modelo
params, _ = curve_fit(modelo_polinomial, x, y)
a, b, c = params

# Previsão para x = 65536
x_pred = 65536
y_pred = modelo_polinomial(x_pred, a, b, c)
y_real = 95823  # Valor conhecido

# Simulação estocástica (Itô simplificado)
np.random.seed(42)
N = 100
t = np.linspace(x[-1], x_pred, N)
dt = (x_pred - x[-1]) / N
dW = np.random.normal(0, np.sqrt(dt), size=N)
W = np.cumsum(dW)

# Processo estocástico: y(t) = f(t) + sigma * W(t)
sigma = 0.1 * y_pred
y_sim = modelo_polinomial(t, a, b, c) + sigma * W

# DataFrame para gráfico
df_plot = pd.DataFrame({
    'x': np.concatenate((x, t)),
    'y': np.concatenate((y, y_sim)),
    'Tipo': ['Real'] * len(x) + ['Simulado (Itô)'] * len(t)
})

# DataFrame de comparação
tabela_comparacao = pd.DataFrame({
    'x': list(x) + [x_pred],
    'y_observado': list(y) + [y_real],
    'y_previsto': list(modelo_polinomial(x, a, b, c)) + [y_pred]
})
tabela_comparacao['erro_absoluto'] = abs(tabela_comparacao['y_previsto'] - tabela_comparacao['y_observado'])

# Gráfico interativo
fig = px.scatter(df_plot, x='x', y='y', color='Tipo',
                 title='Ajuste de y=f(x) com simulação estocástica (Teorema de Itô)',
                 labels={'x': 'x (potências de 2)', 'y': 'y'},
                 hover_data={'x': True, 'y': True, 'Tipo': True})
fig.update_traces(marker=dict(size=6))
fig.show()

# Exibir a tabela de comparação
print("\nÚltimas entradas da tabela de comparação:")
print(tabela_comparacao.tail(6).to_string(index=False))
