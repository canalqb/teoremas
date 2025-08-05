# 📊 Script: `destacar_numero_irracional.py`

## Sobre o Script

Este script **imprime todos os números inteiros em um intervalo definido pelo usuário** e destaca um número específico dentro desse intervalo. O número destacado, neste exemplo, é uma aproximação do produto de um número inteiro pelo número irracional √2.

---

## 🧮 Teorema Aplicado: *Irracionalidade de* √2

O **Teorema da Irracionalidade de √2** afirma que a raiz quadrada de 2 **não pode ser expressa como uma fração exata entre dois números inteiros** — ela é um número irracional.

No script, usamos essa propriedade para **destacar um número inteiro aproximado da multiplicação de √2 por um valor inteiro**, ilustrando que essa aproximação nunca será uma fração exata, apenas uma aproximação.

---

## 📝 Código principal

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
```

---

## 🔧 Possíveis melhorias

* **Interface de entrada:** permitir que o usuário insira o intervalo e o número a destacar dinamicamente.
* **Destaque visual:** usar cores no terminal para destacar o número (bibliotecas como `colorama` podem ajudar).
* **Eficiência:** para intervalos muito grandes, imprimir todos os números pode ser lento — uma solução pode ser imprimir apenas números selecionados ou pular alguns.
* **Mais contexto matemático:** adicionar verificações para múltiplos de aproximações racionais para √2.

---

## 📬 Contato

Feito por [**CanalQb no GitHub**](https://github.com/canalqb)
Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com/)
💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
