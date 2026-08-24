import numpy as np
from scipy.optimize import curve_fit
import plotly.graph_objs as go

# Dados fornecidos
dados = [
    (1, 1, 1), (2, 3, 3), (4, 7, 7), (8, 8, 15),
    (16, 21, 31), (32, 49, 63), (64, 76, 127), (128, 224, 255),
    (256, 467, 511), (512, 514, 1023), (1024, 1155, 2047),
    (2048, 2683, 4095), (4096, 5216, 8191), (8192, 10544, 16383),
    (16384, 26867, 32767), (32768, 51510, 65535)
]

# Separando colunas
x = np.array([p[0] for p in dados])
y = np.array([p[1] for p in dados])
z = np.array([p[2] for p in dados])

# Modelo a ajustar: y = a * x^b + c
def modelo(x, a, b, c):
    return a * x**b + c

# Ajuste dos parâmetros
params, _ = curve_fit(modelo, x, y)

# Previsão para x=65536
x_novo = 65536
y_pred = modelo(x_novo, *params)

# Imprimindo tabela comparativa
print(f"{'x':>10} | {'y (real)':>10} | {'y (previsto)':>14} | {'z':>10}")
print("-"*52)
for xi, yi, zi in zip(x, y, z):
    y_calc = modelo(xi, *params)
    print(f"{xi:10d} | {yi:10d} | {y_calc:14.2f} | {zi:10d}")

print("-"*52)
print(f"{x_novo:10d} | {'?':>10} | {y_pred:14.2f} | {131071:10d}")
print(f"Valor conhecido de y para x=65536: 95823")
print(f"Valor previsto pelo modelo: {y_pred:.2f}")

# Gráfico interativo com plotly
fig = go.Figure()

# Pontos reais
fig.add_trace(go.Scatter(
    x=x, y=y, mode='markers+text',
    text=[f"y={yi}" for yi in y],
    textposition='top center',
    name='Dados reais',
    marker=dict(size=8, color='blue')
))

# Curva do modelo ajustado
x_smooth = np.linspace(min(x), max(max(x), x_novo), 300)
y_smooth = modelo(x_smooth, *params)

fig.add_trace(go.Scatter(
    x=x_smooth, y=y_smooth, mode='lines',
    name='Modelo ajustado',
    line=dict(color='red')
))

# Ponto previsto
fig.add_trace(go.Scatter(
    x=[x_novo], y=[y_pred], mode='markers+text',
    text=[f"Previsto y={y_pred:.0f}"],
    textposition='top center',
    marker=dict(size=10, color='green'),
    name='Previsão'
))

fig.update_layout(
    title='Ajuste do modelo y = a * x^b + c',
    xaxis_title='x',
    yaxis_title='y',
    hovermode='closest'
)

fig.show()
