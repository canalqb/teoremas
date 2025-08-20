import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# Dados fornecidos (x, y, z)
dados = [
    (1, 1, 1), (2, 3, 3), (4, 7, 7), (8, 8, 15), (16, 21, 31), 
    (32, 49, 63), (64, 76, 127), (128, 224, 255), (256, 467, 511), 
    (512, 514, 1023), (1024, 1155, 2047), (2048, 2683, 4095), 
    (4096, 5216, 8191), (8192, 10544, 16383), (16384, 26867, 32767), 
    (32768, 51510, 65535)
]

# Mostrar tabela formatada
print(f"{'x':>8} | {'y':>8} | {'z':>8}")
print("-" * 27)
for x, y, z in dados:
    print(f"{x:8} | {y:8} | {z:8}")

# Extrair vetores para ajuste
x_vals = np.array([d[0] for d in dados])
y_vals = np.array([d[1] for d in dados])

# Ajuste: modelo polinomial de grau 2 (quadrático)
coef = np.polyfit(x_vals, y_vals, deg=2)
poly = np.poly1d(coef)

# Prever último valor (x=65536)
x_next = 65536
y_pred = poly(x_next)

print("\nModelo ajustado: y = {:.6f} x² + {:.6f} x + {:.6f}".format(coef[0], coef[1], coef[2]))
print(f"Previsão para x={x_next}: y ≈ {int(y_pred)}")
print("Valor real informado para comparação: y = 95823")

# Criar DataFrame para gráfico interativo
df = pd.DataFrame(dados, columns=['x', 'y', 'z'])
df.loc[len(df)] = [x_next, int(y_pred), 131071]

# Gráfico interativo com Plotly
fig = px.scatter(df, x='x', y='y', text=df.index,
                 labels={'x': 'x (potências de 2)', 'y': 'y (variável de interesse)'},
                 title='Gráfico interativo de y em função de x')

fig.update_traces(mode='markers+text', textposition='top center',
                  hovertemplate='<b>Índice %{text}</b><br>x: %{x}<br>y: %{y}<extra></extra>')

fig.show()
