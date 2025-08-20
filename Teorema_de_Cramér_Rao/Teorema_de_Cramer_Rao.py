import numpy as np
import plotly.graph_objects as go

# Dados
dados = [
    (1, 1, 1), (2, 3, 3), (4, 7, 7), (8, 8, 15), (16, 21, 31), (32, 49, 63),
    (64, 76, 127), (128, 224, 255), (256, 467, 511), (512, 514, 1023),
    (1024, 1155, 2047), (2048, 2683, 4095), (4096, 5216, 8191),
    (8192, 10544, 16383), (16384, 26867, 32767), (32768, 51510, 65535),
]

# Converter para arrays numpy
x = np.array([d[0] for d in dados])
y = np.array([d[1] for d in dados])
z = np.array([d[2] for d in dados])

# Ajustar polinômio de grau 2 (melhor compromisso entre ajuste e simplicidade)
coef = np.polyfit(x, y, 2)
poly = np.poly1d(coef)

# Prever y para x = 65536
x_pred = 65536
y_pred = poly(x_pred)

# Valor conhecido real de y para comparação
y_real = 95823

# Simular intervalo baseado no Teorema de Cramér-Rao
# Aqui usaremos a variância dos resíduos para simular a "precisão mínima"
residuos = y - poly(x)
var_min = np.var(residuos)
std_min = np.sqrt(var_min)

# Criar intervalo de confiança simulado
intervalo_sup = y_pred + 2*std_min
intervalo_inf = y_pred - 2*std_min

# Tabela de comparação
print("Tabela de Comparação:")
print(f"{'x':>8} {'y observado':>12} {'y ajustado':>12} {'z':>8}")
for xi, yi, zi in zip(x, y, z):
    print(f"{xi:8d} {yi:12d} {int(poly(xi)):12d} {zi:8d}")

print(f"\nPrevisão para x = {x_pred}:")
print(f"y previsto = {int(y_pred)}")
print(f"Intervalo de confiança estimado: [{int(intervalo_inf)}, {int(intervalo_sup)}]")
print(f"Valor real conhecido: {y_real}")

# Gráfico interativo com legendas ao passar o mouse
fig = go.Figure()

# Pontos originais
fig.add_trace(go.Scatter(
    x=x, y=y,
    mode='markers',
    name='Dados Observados (y)',
    text=[f"x={xi}, y={yi}, z={zi}" for xi, yi, zi in zip(x, y, z)],
    hoverinfo='text'
))

# Curva ajustada
x_fit = np.linspace(min(x), x_pred * 1.05, 300)

y_fit = poly(x_fit)

fig.add_trace(go.Scatter(
    x=x_fit, y=y_fit,
    mode='lines',
    name='Curva Ajustada',
))

# Ponto previsto
fig.add_trace(go.Scatter(
    x=[x_pred], y=[y_pred],
    mode='markers',
    marker=dict(color='red', size=12),
    name='Previsão para x=65536',
    text=[f"x={x_pred}, y previsto={int(y_pred)}"],
    hoverinfo='text'
))

# Intervalo de confiança (simulado)
fig.add_trace(go.Scatter(
    x=np.concatenate([x_fit, x_fit[::-1]]),
    y=np.concatenate([y_fit + 2*std_min, (y_fit - 2*std_min)[::-1]]),
    fill='toself',
    fillcolor='rgba(255, 0, 0, 0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    hoverinfo='skip',
    showlegend=True,
    name='Intervalo de Confiança (Simulado)'
))

fig.update_layout(
    title="Ajuste de y em função de x com Intervalo de Confiança baseado no Teorema de Cramér–Rao",
    xaxis_title='x (Potências de 2)',
    yaxis_title='y',
    hovermode='closest'
)

fig.show()
