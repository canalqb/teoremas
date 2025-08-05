📐 **Projeto: Gerador de Ternas Pitagóricas** 
---

🎯 **Descrição**

Este script Python gera todas as **ternas pitagóricas primitivas** $a, b, c$ dentro de um intervalo especificado de valores de **hipotenusa $c$**.

Uma *terna pitagórica* satisfaz a equação:
**a² + b² = c²**, com **a**, **b** e **c** inteiros positivos.

O algoritmo utiliza a fórmula clássica para gerar ternas pitagóricas primitivas:

* a = m² - n²
* b = 2mn
* c = m² + n²

Com *m > n*, *(m - n) ímpar* e *m, n coprimos* (i.e., gcd(m, n) = 1).

---

⚙️ **Funcionamento**

O script percorre os valores de **m** e **n** para gerar ternas primitivas e verifica se o valor de **c** está dentro de um intervalo desejado.
No trecho incluído, os intervalos são definidos como potências de 2:

* 2⁰ a 2¹ − 1
* 2¹ a 2² − 1
* 2² a 2³ − 1
* ...
* até 2⁹ a 2¹⁰ − 1

Para cada intervalo, o programa imprime todas as ternas $(a, b, c)$ encontradas.

---

📦 **Saída esperada**

Para cada intervalo, o script imprime:

`<potência> -> a = <valor>, b = <valor>, c = <valor>`

Exemplo:

```
3 -> a = 7, b = 24, c = 25
4 -> a = 15, b = 8, c = 17
```

---

🧠 **Aplicações**

* Ensino de matemática
* Demonstração visual de conceitos de geometria
* Verificação de propriedades numéricas
* Criação de conjuntos de dados matemáticos

---

🛠️ **Requisitos**

* Python 3.x
* Nenhuma biblioteca externa (usa apenas `math.gcd`)

---

📈 **Possíveis melhorias futuras**

* Exportar as ternas para arquivos `.csv` ou `.json`
* Gerar também *ternas não primitivas*
* Adicionar interface gráfica ou visualização interativa
* Visualizar ternas em um gráfico cartesiano

---

💡 *Este script é ideal para quem deseja explorar os números inteiros sob uma ótica geométrica e algébrica ao mesmo tempo!*

---

## 📬 Contato

Feito por [CanalQb no GitHub](https://github.com/canalqb)
Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com/)
💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`

