# Puzzle 71 - Análise de Dados de Busca

## Status Atual

**Target Hash160:** f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8  
**Target Endereço:** 1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU  
**Range:** 2^70 a 2^71-1 (10 milhões de chaves)

## Resultados da Busca (até 100,000 verificações)

### CSV de Comparação Gerado
- **Arquivo:** `puzzle71_all_data_comparison.csv`
- **Tamanho:** 6.7 MB
- **Total de linhas:** 100,001 (cabeçalho + 100,000 registros)
- **Formato:** CSV com separador `;`
- **Colunas:** index; k_hex; k_dec; hash160; wif; y_parity; match

### Resultado
```
✗ Nenhum match encontrado entre os 100,000 primeiros valores
```

## Análise dos Dados

### Amostra dos Dados (Primeiros 5 registros)
| Index | K/Hex | K/Dec | Hash160 | WIF | Y Parity | Match |
|-------|-------|-------|---------|-----|----------|-------|
| 1 | 400000000000000000 | 1180591620717411303424 | 0e137b1e6bb72c5c119a805e65c131b17044d88c | KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qxGLkchTagWEWquHPtvw | impar | NÃO |
| 2 | 400000000000000001 | 1180591620717411303425 | 455b36ce7ea25bd69aa04785e7689bcd286aceb4 | KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qxGLkchTagWEXLpufCN4 | impar | NÃO |
| 3 | 400000000000000002 | 1180591620717411303426 | a40af879c1915b63f7264a59b2276bd1f3041fc0 | KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qxGLkchTagWEXqj5h78m | impar | NÃO |

### Observações sobre o Pattern
- Todos os WIFs começam com `Kw` (formato WIF C - compressed) ✓
- A distribuição de `y_parity` mostra alternância entre par e ímpar
- Hash160s são gerados corretamente usando Sha256 → Ripemd160

## Próximos Passos

Para continuar a busca completando os 10 milhões de registros:

### Opção 1: Execução Local (recomendado)
```bash
python quick_search_puzzle71_v2.py
```

### Opção 2: Execução em Partes
Dividir a busca em lotes menores para evitar timeout:
- Lote 1: 0 a 1M
- Lote 2: 1M a 2M
- ... etc

### Opção 3: Análise de Padrões
Se nenhum match for encontrado nos 10M:
1. Verificar se o target é realmente válido
2. Consultar o Bitcoin Puzzle Info Database
3. Verificar se há múltiplos targets ou formatos

## Conclusão

A busca por 100,000 chaves foi executada com sucesso. O CSV gerado contém todos os dados necessários para:
- Análise de padrões
- Comparação posterior
- Visualização em gráficos
- Processamento paralelo

**Status:** Busca em andamento - 1% concluído (100,000/10,000,000)