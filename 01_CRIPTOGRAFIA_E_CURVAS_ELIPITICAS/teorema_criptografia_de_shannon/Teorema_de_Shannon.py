import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Dados fornecidos
dados = [
    (1, 1, 1), (2, 3, 3), (4, 7, 7), (8, 8, 15), (16, 21, 31), (32, 49, 63), (64, 76, 127),
    (128, 224, 255), (256, 467, 511), (512, 514, 1023), (1024, 1155, 2047), (2048, 2683, 4095),
    (4096, 5216, 8191), (8192, 10544, 16383), (16384, 26867, 32767), (32768, 51510, 65535)
]

# Preparar dados
df = pd.DataFrame(dados, columns=["x", "y", "z"])

# Ajustar modelo polinomial para prever y com base em x
X = df[["x"]]
y = df["y"]
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)

# Prever os valores de y
df["y_pred"] = model.predict(X_poly).round().astype(int)

# Prever y para x = 65536
x_novo = np.array([[65536]])
x_novo_poly = poly.transform(x_novo)
y_novo_pred = model.predict(x_novo_poly)[0]

# Adicionar ponto previsto
df_extended = df.copy()
df_extended.loc[len(df_extended)] = [65536, 95823, 131071, round(y_novo_pred)]

# Exibir tabela
print(df_extended.to_string(index=False))

# Gráfico interativo
fig = px.scatter(df_extended, x="x", y="y", text=df_extended.index,
                 labels={"x": "x (Potência de 2)", "y": "y (Capacidade observada)"},
                 title="Capacidade do Canal vs x segundo o Teorema de Shannon 📶",
                 hover_data={"x": True, "y": True, "y_pred": True, "z": True})
fig.add_scatter(x=df_extended["x"], y=df_extended["y_pred"], mode="lines", name="Ajuste Polinomial (Grau 2)")
fig.update_traces(marker=dict(size=10))
fig.update_layout(hovermode="closest")
fig.show()
