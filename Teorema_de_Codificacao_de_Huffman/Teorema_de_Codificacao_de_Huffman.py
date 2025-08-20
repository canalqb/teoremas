import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Dados fornecidos
dados = [
    (1, 1, 1), (2, 3, 3), (4, 7, 7), (8, 8, 15), (16, 21, 31),
    (32, 49, 63), (64, 76, 127), (128, 224, 255), (256, 467, 511),
    (512, 514, 1023), (1024, 1155, 2047), (2048, 2683, 4095),
    (4096, 5216, 8191), (8192, 10544, 16383), (16384, 26867, 32767),
    (32768, 51510, 65535)
]

# Conversão em DataFrame
df = pd.DataFrame(dados, columns=["x", "y", "z"])

# Ajuste polinomial de grau 2
X = df[['x']]
y = df['y']

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

# Predição para todos os x + previsão de y para x=65536
x_pred = np.append(df['x'].values, 65536)
X_pred_poly = poly.transform(x_pred.reshape(-1, 1))
y_pred = model.predict(X_pred_poly)

# Adicionando o ponto previsto
df_pred = df.copy()
df_pred.loc[len(df_pred.index)] = [65536, round(y_pred[-1]), 131071]  # Valor real de z

# Mostrando a tabela no console
print(df_pred.to_string(index=False))

# Gráfico interativo
df_plot = df.copy()
df_plot['Label'] = df_plot.apply(lambda row: f"x: {row['x']}, y: {row['y']}, z: {row['z']}", axis=1)
df_plot['y_pred'] = y_pred[:-1]

fig = px.scatter(df_plot, x='x', y='y', text='Label', title="Ajuste de y em função de x (Teorema de Huffman 📊)")
fig.add_scatter(x=df_plot['x'], y=df_plot['y_pred'], mode='lines', name='Modelo Polinomial (Grau 2)')
fig.update_traces(textposition='top center', hoverinfo='text')
fig.update_layout(hovermode='closest')

fig.show()
