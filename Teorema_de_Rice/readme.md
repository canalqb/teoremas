# Estimativa de Funções sob o Teorema de Rice

Este repositório apresenta uma explicação concisa do **Teorema de Rice** e um script que utiliza esse conceito para estimar, de forma empírica, a quantidade de funções com propriedades não triviais dentro de um intervalo específico de complexidade (medido como números entre `2^N` e `2^(N+1) - 1`).

## 📘 O que é o Teorema de Rice?

O **Teorema de Rice**, proposto por Henry Gordon Rice em 1953, é um dos resultados fundamentais da teoria da computação. Ele afirma:

> **Toda propriedade semântica não trivial de linguagens reconhecíveis por máquinas de Turing é indecidível.**

### Em termos práticos:
- Não existe um algoritmo geral que determine se uma máquina de Turing (ou programa) exibe determinada propriedade comportamental — como "termina", "imprime algo", "aceita determinada entrada", etc.
- Uma propriedade é **não trivial** se não se aplica a todas nem a nenhuma função computável.

### Consequência:
Mesmo que não possamos decidir se uma função tem ou não determinada propriedade, podemos tentar **estimar**, **contar** ou **aproximar** quantas funções possivelmente exibem essa propriedade dentro de um espaço finito.

---

## 🧮 Sobre o script

O script `estimativa_rice.py` aplica uma **abordagem empírica** para estimar quantas funções (ou programas) entre `2^N` e `2^(N+1)-1` podem possuir uma propriedade não trivial (por exemplo, serem computáveis, aceitarem entrada, terminarem, etc.), mesmo sem decidibilidade exata — em conformidade com o Teorema de Rice.

### Estratégia usada:
- Define um intervalo crescente entre `2^N` e `2^(N+1) - 1`.
- Usa uma função baseada em `log2` para simular a filtragem de funções triviais e aproximar as que podem apresentar uma propriedade não trivial.
- Retorna uma tabela comparativa com:
  - `N`: o nível de complexidade
  - `Início`: o valor `2^N`
  - `Fim`: o valor `2^(N+1) - 1`
  - `Estimado`: aproximação de quantas funções dentro do intervalo possuem uma propriedade que não pode ser decidida (mas pode ser inferida numericamente).

### Exemplo de saída:
```

## N  | Início (2^N)  | Fim (2^(N+1)-1)  | Estimado

0  | 1             | 2                | 1
1  | 2             | 4                | 3
2  | 4             | 8                | 7
3  | 8             | 16               | 11
4  | 16            | 32               | 24
...

```

### Por que isso é útil?
Esse tipo de estimativa serve como base para:
- Análises experimentais em **teoria da computação**;
- Estudos de **complexidade algorítmica**;
- Avaliações empíricas de propriedades em **sistemas formais** onde a decidibilidade não é possível;
- Simulações de comportamentos computacionais sob limites definidos.

---

## ⚠️ Limitações

- O Teorema de Rice afirma que **não é possível determinar com certeza** se funções arbitrárias têm ou não uma propriedade.
- Portanto, o script **não decide** propriedades, mas **modela** e **estima quantitativamente** seu comportamento dentro de domínios finitos.

---

## 📂 Arquivo principal

- `estimativa_rice.py`: Gera a tabela de estimativas para cada N de 0 a 9.

---

## 📜 Licença

Este projeto é de domínio educacional e pode ser usado livremente com fins acadêmicos.

--- 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
