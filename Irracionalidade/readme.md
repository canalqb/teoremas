# 📐 - Teorema *Irracionalidade de* √2

## 🧾 Frase do Teorema

> A raiz quadrada de 2 **não pode ser expressa como uma fração exata entre dois números inteiros** – ou seja, √2 é um número irracional, não representável por uma fração simples.

## 📚 Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `destacar_numero_irracional.py`](#2-script-destacar_numero_irracionalpy)
  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3 Extras](#3-extras)
  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referencias)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4 📬 Contato](#4-📬-contato)
* [5. Nota](#5-nota)

---

# 1. Introdução ao Teorema

## 1.1 Resumo

O **Teorema da Irracionalidade de √2** mostra que √2 não pode ser escrito como uma fração exata entre dois inteiros. Isso implica que não há números inteiros `a` e `b` tais que `a/b = √2`.

## 1.2 Exemplos Práticos

Um exemplo prático é a multiplicação de um inteiro por √2, que sempre resultará em um número irracional, aproximado por um número inteiro.

## 1.3 Explicação Detalhada

Historicamente, provou-se por contradição que não existem números inteiros que formem a fração exata para √2. Portanto, essa raiz é considerada um número *irracional*.

## 1.4 Aplicações

Esta propriedade é essencial na matemática, física e engenharia, principalmente em problemas que envolvem medidas que não são múltiplos exatos de uma unidade racional.

## 1.5 Análise da Tabela

Neste repositório, não há tabelas específicas, mas o script imprime uma sequência de números inteiros, destacando a aproximação de √2 multiplicada por um inteiro.

---

# 2. Script `destacar_numero_irracional.py`

## 2.1 Relação com o Teorema

O script utiliza a propriedade da irracionalidade de √2 para destacar um número inteiro aproximado do produto entre um número inteiro e √2, ilustrando a impossibilidade de representá-lo exatamente como uma fração.

## 2.2 Objetivo do Script

Imprimir todos os números inteiros em um intervalo definido e destacar o número que é a aproximação da multiplicação do inteiro pelo número irracional √2.

## 2.3 Exemplo de Saída


```
2048
2049
...
2896 <-- número destacado!
...
4096
Total: 2049 números gerados

``` 

*Nota:* O número destacado é a aproximação de `2048 * √2`.

## 2.4 Funcionamento Interno

```python
def imprimir_intervalo_e_destacar(numero_destaque, inicio, fim):
    """
    Imprime números no intervalo [inicio, fim].
    Destaca um número específico.
    
    Args:
        numero_destaque (int): Número a ser destacado na impressão.
        inicio (int): Início do intervalo.
        fim (int): Fim do intervalo.
    """
    contador = 0
    for n in range(inicio, fim + 1):
        if n == numero_destaque:
            print(f"{n} <-- número destacado!")
        else:
            print(n)
        contador += 1
    print(f"Total: {contador} números gerados")

import math
numero_destaque = round(2048 * math.sqrt(2))  # aproximação de sqrt(2)*2048
imprimir_intervalo_e_destacar(numero_destaque, 2048, 4096)
````

## 2.5 Tecnologias e Requisitos

* Python 3.x
* Biblioteca padrão `math`

---

# 3 Extras

## 3.1 Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

## 3.2 Referências

* [Irrationality of √2 - Wikipedia](https://en.wikipedia.org/wiki/Proof_that_sqrt%282%29_is_irrational)
* CanalQb Blog: [https://canalqb.blogspot.com](https://canalqb.blogspot.com)

## 3.3 Testes e Validações

Testado em Python 3.8+ para assegurar que o número destacado corresponde corretamente à aproximação de `√2` multiplicado pelo inteiro.

---

## 4 📬 Contato

* Feito por CanalQb no GitHub
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

# 5. Nota

Este README foi construído para documentar o teorema e o script de forma clara, didática e acessível, com intuito educacional e para facilitar o uso e entendimento do código.

---

```

Se quiser, posso ajudar a formatar algum trecho ou criar versões em outras línguas! Quer fazer algo mais?
```
