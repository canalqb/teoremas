import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Dados fornecidos
dados = [
    (1, 1, 1), (2, 3, 3), (4, 7, 7), (8, 8, 15), (16, 21, 31), (32, 49, 63),
    (64, 76, 127), (128, 224, 255), (256, 467, 511), (512, 514, 1023),
    (1024, 1155, 2047), (2048, 2683, 4095), (4096, 5216, 8191),
    (8192, 10544, 16383), (16384, 26867, 32767), (32768, 51510, 65535)
]

# Criar DataFrame
df = pd.DataFrame(dados, columns=['x', 'y', 'z'])

print("Tabela de comparação:")
print(df)

# Ajuste polinomial para y ~ x
X = df['x'].values.reshape(-1,1)
y = df['y'].values

# Usar polinômio grau 2 para tentar captar crescimento não linear
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

# Previsão para x = 65536
x_new = np.array([[65536]])
x_new_poly = poly.transform(x_new)
y_pred = model.predict(x_new_poly)[0]

print(f"\nPrevisão do modelo para x=65536: y = {y_pred:.0f}")
print(f"Valor real conhecido: y = 95823")

# Simulação baseada no teorema de Girsanov (simplificada):
# Suponha que y é uma média + ruído com deriva ajustada
np.random.seed(42)
n_sim = 1000
drift = model.predict(poly.transform(X))
drift_new = model.predict(x_new_poly)

# Simula ruído gaussiano com média zero
noise = np.random.normal(0, 5000, n_sim)
simulacoes = drift_new + noise

# Visualização interativa dos dados originais e previsão
df_plot = df.copy()
df_plot['tipo'] = 'Original'

df_sim = pd.DataFrame({
    'x': 65536,
    'y': simulacoes,
    'tipo': 'Simulação'
})

df_all = pd.concat([df_plot, df_sim], ignore_index=True)

fig = px.scatter(df_all, x='x', y='y', color='tipo',
                 title="Modelo e Simulação de y em função de x",
                 labels={"x":"x (potência de 2)", "y":"y (variável de interesse)"},
                 hover_data={'x':True, 'y':True, 'tipo':True})

fig.update_traces(marker=dict(size=8))

fig.show()
