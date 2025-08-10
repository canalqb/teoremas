# Infinitude dos primos

Este repositório contém uma implementação em Python que ilustra, de forma prática, a **infinitude dos números primos**, conforme demonstrado por **Euclides** por volta de 300 a.C.

Através de uma abordagem computacional simples, o script `Infinitude_dos_primos.py` simula o argumento clássico:  
> "Seja uma lista de primos conhecidos. Multiplicando todos eles e somando 1 ao produto, o número resultante ou é primo, ou possui fatores primos que não estavam na lista inicial."

## Objetivo

Demonstrar que:
- Sempre é possível encontrar mais primos além de uma lista finita conhecida.
- O conjunto dos números primos é infinito.

## Como o Script Funciona

O script realiza os seguintes passos:

1. **Geração de primos**: Utiliza o Crivo de Eratóstenes para gerar todos os primos dentro de intervalos da forma `[2^i, 2^{i+1} - 1]`, para `i` de 0 até 4.
2. **Atualização do conjunto de primos conhecidos**: Os primos encontrados são acumulados em um conjunto.
3. **Produto dos primos + 1 (Euclides)**: Calcula o produto de todos os primos conhecidos até o momento e adiciona 1.
4. **Verificação de primalidade**: Checa se o número resultante (`produto + 1`) é primo ou composto.
5. **Exibição em tabela**: Apresenta uma tabela com o intervalo avaliado, a quantidade de primos encontrados e o resultado da verificação do número `produto + 1`.

### Exemplo de Saída

```bash
* ID | Intervalo | Qtd. de Primos | Produto + 1 (Euclides)
* 0 | [1, 1]:^17 | 0 | -
* 1 | [2, 3]:^17 | 2 | 7 (Primo)
* 2 | [4, 7]:^17 | 1 | 43 (Primo)
* 3 | [8, 15]:^17 | 2 | 1807 (Primo)
* 4 | [16, 31]:^17 | 5 | 3263443 (Primo) 
```

> Observação: a saída acima é apenas um exemplo e pode variar conforme o número de intervalos analisados.

## Arquivo Principal

### [`Infinitude_dos_primos.py`](./Infinitude_dos_primos.py)

Contém todo o código para:
- Gerar primos com o Crivo de Eratóstenes.
- Calcular o produto dos primos.
- Verificar se `produto + 1` é primo.
- Exibir os resultados em formato de tabela.

## Requisitos

- Python 3.6+
- Nenhuma biblioteca externa é necessária (apenas `math`, da biblioteca padrão).

## Como Executar

```bash
python Infinitude_dos_primos.py
Licença
Este projeto está licenciado sob a MIT License.
``` 
---

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com 
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
