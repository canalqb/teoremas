import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Dados
dados = [ 
  (1, 1, 1), (2, 3, 3), (4, 7, 7), (8, 8, 15), (16, 21, 31), (32, 49, 63), (64, 76, 127), 
  (128, 224, 255), (256, 467, 511), (512, 514, 1023), (1024, 1155, 2047), (2048, 2683, 4095), 
  (4096, 5216, 8191), (8192, 10544, 16383), (16384, 26867, 32767), (32768, 51510, 65535)
]

# Separando colunas
x = np.array([d[0] for d in dados])
y = np.array([d[1] for d in dados])
z = np.array([d[2] for d in dados])

# Ajuste polinomial grau 2 (y ~ x)
coef = np.polyfit(x, y, 2)
poly = np.poly1d(coef)

# Previsão para o conjunto de dados e para x=65536
y_pred = poly(x)
x_novo = 65536
y_novo_pred = poly(x_novo)
y_novo_real = 95823  # dado pelo usuário

# Impressão da tabela comparativa
print(f"{'x':>8} {'y_real':>10} {'y_pred':>10}")
for xi, yi_real, yi_pred in zip(x, y, y_pred):
    print(f"{xi:8d} {yi_real:10d} {int(yi_pred):10d}")
print(f"{x_novo:8d} {y_novo_real:10d} {int(y_novo_pred):10d} (Previsão)")

# Gráfico interativo com plotly
trace_real = go.Scatter(
    x=x, y=y, mode='markers+lines', name='y real',
    text=[f"x={xi}, y={yi}" for xi, yi in zip(x, y)],
    hoverinfo='text'
)
trace_pred = go.Scatter(
    x=x, y=y_pred, mode='lines', name='y previsto (modelo)',
    line=dict(dash='dash')
)
trace_novo = go.Scatter(
    x=[x_novo], y=[y_novo_real], mode='markers', name='Novo ponto real',
    marker=dict(color='red', size=10),
    text=[f"x={x_novo}, y={y_novo_real} (real)"],
    hoverinfo='text'
)
trace_novo_pred = go.Scatter(
    x=[x_novo], y=[y_novo_pred], mode='markers', name='Novo ponto previsto',
    marker=dict(color='green', size=10),
    text=[f"x={x_novo}, y={int(y_novo_pred)} (previsto)"],
    hoverinfo='text'
)

fig = go.Figure(data=[trace_real, trace_pred, trace_novo, trace_novo_pred])
fig.update_layout(title="Ajuste de modelo y = f(x) pelo Teorema de Gauss-Markov",
                  xaxis_title="x",
                  yaxis_title="y",
                  hovermode="closest")

fig.show()
