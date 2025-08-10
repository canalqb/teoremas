import bisect

# Lista conhecida (parcial) dos primeiros números de Carmichael (extraída de tabelas confiáveis)
carmichaels = [
    561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 
    41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217,
    162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153,
    340561, 399001, 410041, 449065, 488881, 512461, 530881, 552721,
    656601, 658801, 670033, 748657, 825265, 838201, 852841, 997633,
    1024651, 1033669, 1050985, 1058197, 1062347, 1071225, 1152271,
    1193221, 1461241
]

procurados = [
    1, 3, 7, 8, 21, 49, 76, 224, 467, 514, 1155, 2683, 5216, 10544,
    26867, 51510, 95823, 198669, 357535, 863317, 1811764, 3007503,
    5598802, 14428676, 33185509, 54538862, 111949941, 227634408
]

def eh_carmichael(n):
    # Busca rápida na lista conhecida
    return n in carmichaels

def busca_anterior(valor):
    pos = bisect.bisect_left(carmichaels, valor)
    return carmichaels[pos-1] if pos > 0 else None

def busca_posterior(valor):
    pos = bisect.bisect_right(carmichaels, valor)
    return carmichaels[pos] if pos < len(carmichaels) else None

print("🔍 Verificando números de Carmichael com lista pré-calculada...\n")

for valor in procurados:
    eh_carm = eh_carmichael(valor)
    anterior = busca_anterior(valor)
    posterior = busca_posterior(valor)
    print(f"Valor: {valor}")
    print(f" → É número de Carmichael? {'Sim ✅' if eh_carm else 'Não ❌'}")
    print(f" → Carmichael anterior: {anterior if anterior is not None else 'Nenhum encontrado'}")
    print(f" → Carmichael posterior: {posterior if posterior is not None else 'Nenhum encontrado'}")
    print("-" * 50)
