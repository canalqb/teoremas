# 📊 Validação do Teorema Central do Limite (TCL)

Este repositório contém um script simples de simulação para ilustrar o funcionamento do **Teorema Central do Limite (TCL)** usando amostras de uma distribuição normal padrão.

---

## 📘 O que é o Teorema Central do Limite?

O **Teorema Central do Limite** afirma que:

> Dada qualquer distribuição populacional com média μ e desvio padrão σ, a média de amostras suficientemente grandes tenderá a seguir uma **distribuição normal**, independentemente do formato da distribuição original.

Em termos práticos:
- Quanto maior o tamanho da amostra (`n`), mais próxima da normal será a distribuição das médias.
- A variabilidade da média amostral diminui com o aumento de `n`, seguindo a fórmula:
  \[
  \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
  \]

---

## 🧪 Objetivo do Script

O script `valida_tcl_intervalos.py` realiza simulações para mostrar como a média de amostras de tamanhos crescentes se comporta com relação a um intervalo de confiança próximo à média real (μ = 0).

| Início | Procuras | Fim | Tamanho da Amostra |
|--------|----------|-----|--------------------|
| 1      | 1        | 2   | 1                  |
| 2      | 3        | 4   | 2                  |
| 4      | 7        | 8   | 4                  |
| 8      | 8        | 16  | 8                  |
| 16     | 21       | 32  | 16                 |
| 32     | 49       | 64  | 32                 |
| 64     | 76       | 128 | 64                 |
| 128    | 224      | 256 | 128                |

Para cada linha, o script:
- Gera `procuras` amostras aleatórias do tamanho indicado.
- Calcula a média de cada amostra.
- Verifica se a média está dentro do intervalo `[μ - 0.1, μ + 0.1]`.

---

## 📈 Resultados da Simulação

```text
C:\Users\Notebook\Desktop\teoremas>valida_tcl_intervalos
Validando colunas com base no Teorema Central do Limite:
Amostra de tamanho   1, procuras:   1 -> Proporção dentro do intervalo esperado: 0.00
Amostra de tamanho   2, procuras:   3 -> Proporção dentro do intervalo esperado: 0.33
Amostra de tamanho   4, procuras:   7 -> Proporção dentro do intervalo esperado: 0.00
Amostra de tamanho   8, procuras:   8 -> Proporção dentro do intervalo esperado: 0.38
Amostra de tamanho  16, procuras:  21 -> Proporção dentro do intervalo esperado: 0.24
Amostra de tamanho  32, procuras:  49 -> Proporção dentro do intervalo esperado: 0.41
Amostra de tamanho  64, procuras:  76 -> Proporção dentro do intervalo esperado: 0.63
Amostra de tamanho 128, procuras: 224 -> Proporção dentro do intervalo esperado: 0.63
````

➡️ Os resultados confirmam que, à medida que o tamanho da amostra aumenta, a **proporção de médias próximas da média real também aumenta**, validando empiricamente o Teorema Central do Limite.

---

## 🛠️ Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Instale os pacotes necessários (opcional para visualização):

```bash
pip install numpy matplotlib
```

3. Execute o script:

```bash
python valida_tcl_intervalos.py
```

---

## 📁 Estrutura do Projeto

```
teoremas/
├── valida_tcl_intervalos.py
└── README.md
```

---

## 📚 Referências

* [Khan Academy – Teorema Central do Limite](https://pt.khanacademy.org/math/statistics-probability/sampling-distributions-library)
* [Wikipedia – Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. 

---

  
## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
