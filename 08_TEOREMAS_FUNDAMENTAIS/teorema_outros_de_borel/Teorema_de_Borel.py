import pandas as pd
import numpy as np
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

# Convertendo para DataFrame
df = pd.DataFrame(dados, columns=["x", "y", "z"])

# Ajustando modelo polinomial de grau 2
X = df[["x"]]
y = df["y"]
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression().fit(X_poly, y)

# Previsão para x = 65536
x_future = np.array([[65536]])
x_future_poly = poly.transform(x_future)
y_pred = model.predict(x_future_poly)[0]

# Adiciona ao DataFrame
df_pred = df.copy()
df_pred.loc[len(df)] = [65536, y_pred, 131071]

# Gera gráfico interativo
fig = px.scatter(df_pred, x="x", y="y", text="y", title="Modelagem de y em função de x")
fig.update_traces(mode='markers+lines', hovertemplate='x=%{x}<br>y=%{y}')
fig.update_layout(hovermode='closest')
fig.show()

# Tabela de comparação com valor real
real_y = 95823
df_pred["y_pred"] = model.predict(poly.transform(df_pred[["x"]]))
df_pred["Erro absoluto"] = abs(df_pred["y_pred"] - df_pred["y"])
df_pred.loc[len(df_pred)-1, "y"] = real_y  # Substitui pelo valor real

# Exibe as últimas linhas
print(df_pred.tail())
