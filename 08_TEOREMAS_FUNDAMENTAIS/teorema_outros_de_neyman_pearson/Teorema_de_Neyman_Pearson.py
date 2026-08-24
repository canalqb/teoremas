import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# Dados
dados = [
    (1, 1, 1), (2, 3, 3), (4, 7, 7), (8, 8, 15), (16, 21, 31),
    (32, 49, 63), (64, 76, 127), (128, 224, 255), (256, 467, 511),
    (512, 514, 1023), (1024, 1155, 2047), (2048, 2683, 4095),
    (4096, 5216, 8191), (8192, 10544, 16383), (16384, 26867, 32767),
    (32768, 51510, 65535)
]

# Separar colunas
x = np.array([t[0] for t in dados])
y = np.array([t[1] for t in dados])
z = np.array([t[2] for t in dados])

# Ajuste polinomial de grau 2 (tentativa inicial)
coef = np.polyfit(x, y, 2)
polinomio = np.poly1d(coef)

# Prever y para o último x = 65536
x_pred = 65536
y_pred = polinomio(x_pred)

print(f"Previsão para x={x_pred}: y={int(y_pred)}")
print(f"Valor conhecido: y=95823")

# Mostrar tabela de comparação
print("\nTabela de comparação:")
print(f"{'x':>8} {'y (real)':>10} {'y (predito)':>15} {'z':>8}")
for i in range(len(x)):
    print(f"{x[i]:8} {y[i]:10} {int(polinomio(x[i])):15} {z[i]:8}")

# Para gráfico interativo com plotly, criamos dataframe
df = pd.DataFrame({
    'x': x,
    'y_real': y,
    'y_predito': polinomio(x),
    'z': z,
    'label': [f"x={xi}, y={yi}, z={zi}" for xi, yi, zi in dados]
})

# Gráfico interativo
import plotly.graph_objects as go

fig = go.Figure()

# Pontos reais
fig.add_trace(go.Scatter(
    x=df['x'], y=df['y_real'], mode='markers+lines',
    name='y real', text=df['label'],
    hoverinfo='text+name'
))

# Pontos preditos
fig.add_trace(go.Scatter(
    x=df['x'], y=df['y_predito'], mode='markers+lines',
    name='y predito', text=[f"x={xi}, y_pred={int(yp)}" for xi, yp in zip(df['x'], df['y_predito'])],
    hoverinfo='text+name'
))

fig.update_layout(
    title="Comparação entre y real e y predito (polinomial grau 2)",
    xaxis_title="x (potências de 2)",
    yaxis_title="y",
    hovermode="closest"
)

fig.show()
