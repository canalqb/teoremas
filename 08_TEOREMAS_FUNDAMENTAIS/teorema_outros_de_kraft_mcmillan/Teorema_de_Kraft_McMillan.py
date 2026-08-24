import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression

# Dados fornecidos
dados = [ 
    (1, 1, 1), (2, 3, 3), (4, 7, 7), (8, 8, 15), (16, 21, 31), (32, 49, 63),
    (64, 76, 127), (128, 224, 255), (256, 467, 511), (512, 514, 1023),
    (1024, 1155, 2047), (2048, 2683, 4095), (4096, 5216, 8191),
    (8192, 10544, 16383), (16384, 26867, 32767), (32768, 51515, 65535)
]

# Convertendo para DataFrame
df = pd.DataFrame(dados, columns=["x", "y", "z"])

# Ajuste de modelo: y em função de log2(x)
X = np.log2(df["x"]).values.reshape(-1, 1)
y = df["y"].values
model = LinearRegression()
model.fit(X, y)

# Prevendo para x = 65536
log2_next_x = np.log2(65536)
predicted_y = model.predict([[log2_next_x]])[0]

# Adiciona o valor real conhecido
df.loc[len(df)] = [65536, 95823, 131071]  # y real fornecido

# Criando gráfico interativo
fig = px.scatter(df, x="x", y="y", text=df["x"],
                 title="Modelagem de y em função de x (potências de 2)",
                 labels={"x": "x", "y": "y"},
                 hover_data=["x", "y", "z"])

fig.add_scatter(x=[65536], y=[predicted_y], mode="markers+text",
                text=["y previsto"], name="y previsto (modelo)",
                marker=dict(color="red", size=10))

fig.show()

# Tabela de comparação
df["log2(x)"] = np.log2(df["x"]).astype(int)
df["y previsto (modelo)"] = model.predict(np.log2(df["x"]).values.reshape(-1, 1)).astype(int)
df["erro"] = df["y"] - df["y previsto (modelo)"]
print(df)
