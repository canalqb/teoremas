def gerar_intervalos(n_max):
    intervalos = []
    for n in range(n_max + 1):
        inicio = 2**n
        fim = 2**(n+1) - 1
        intervalos.append((inicio, fim))
    return intervalos

def listar_intervalos(intervalos):
    print("Intervalos gerados:")
    for i, (inicio, fim) in enumerate(intervalos):
        print(f"n={i}: [{inicio}, {fim}]")

def verificar_sobreposicao(intervalos):
    intervalos_ordenados = sorted(intervalos, key=lambda x: x[0])
    sobreposicoes = []
    for i in range(len(intervalos_ordenados) - 1):
        fim_atual = intervalos_ordenados[i][1]
        inicio_proximo = intervalos_ordenados[i+1][0]
        if fim_atual >= inicio_proximo:
            sobreposicoes.append((intervalos_ordenados[i], intervalos_ordenados[i+1]))
    return sobreposicoes

def ponto_medio_extremos(intervalos):
    menor = min([inicio for (inicio, _) in intervalos])
    maior = max([fim for (_, fim) in intervalos])
    meio = (menor + maior) / 2
    return meio

def intercalar_intervalos(intervalos):
    menor = min([inicio for (inicio, _) in intervalos])
    maior = max([fim for (_, fim) in intervalos])
    sequencia_completa = list(range(menor, maior + 1))
    return sequencia_completa

def gerar_pontos_cruzamento(intervalos):
    pontos_cruzamento = []
    intervalos_ordenados = sorted(intervalos, key=lambda x: x[0])
    for i in range(len(intervalos_ordenados) - 1):
        fim_atual = intervalos_ordenados[i][1]
        inicio_proximo = intervalos_ordenados[i+1][0]
        if fim_atual + 1 == inicio_proximo:
            pontos_cruzamento.append((fim_atual, inicio_proximo))
    return pontos_cruzamento

def pontos_internos(intervalos, k_variacao=3):
    pontos = []
    for inicio, fim in intervalos:
        ponto_medio = (inicio + fim) / 2
        # Valores próximos ao número de Mersenne (fim do intervalo), variando até k valores para trás
        mersennes_variados = [fim - k for k in range(k_variacao) if (fim - k) >= inicio]
        pontos.append({
            "intervalo": (inicio, fim),
            "ponto_medio": ponto_medio,
            "mersennes_variados": mersennes_variados
        })
    return pontos

# ======= Execução =======

n_max = 10
intervalos = gerar_intervalos(n_max)

listar_intervalos(intervalos)

sobreposicoes = verificar_sobreposicao(intervalos)
if sobreposicoes:
    print("\nIntervalos que se sobrepõem:")
    for intervalo1, intervalo2 in sobreposicoes:
        print(f"{intervalo1} e {intervalo2}")
else:
    print("\nNão há intervalos que se sobrepõem.")

ponto_medio = ponto_medio_extremos(intervalos)
print(f"\nPonto médio entre os extremos de todos os intervalos: {ponto_medio}")

sequencia = intercalar_intervalos(intervalos)
print(f"\nSequência contínua gerada (de {sequencia[0]} a {sequencia[-1]}), total de {len(sequencia)} números.")

pontos_cruzamento = gerar_pontos_cruzamento(intervalos)
print("\nPontos de cruzamento entre intervalos consecutivos:")
for fim, inicio in pontos_cruzamento:
    print(f"Ponto entre {fim} e {inicio}")

pontos_var = pontos_internos(intervalos)
print("\nPontos internos nos intervalos (ponto médio e variações próximas a Mersenne):")
for info in pontos_var:
    ini, fim = info["intervalo"]
    print(f"Intervalo [{ini}, {fim}]:")
    print(f"  - Ponto médio: {info['ponto_medio']}")
    print(f"  - Próximos de Mersenne (variações): {info['mersennes_variados']}")
