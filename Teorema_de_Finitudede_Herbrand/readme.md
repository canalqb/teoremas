# Teorema de Finitude de Herbrand - Script de Estimativa

Este repositório apresenta uma explicação concisa do **Teorema de Finitude de Herbrand** e um script Python para estimar a quantidade finita de instâncias de Herbrand necessárias até um dado nível N, de acordo com o crescimento exponencial previsto pelo teorema.

---

## O que é o Teorema de Finitude de Herbrand?

O **Teorema de Finitude de Herbrand** é um resultado fundamental na lógica matemática, especialmente na área de **prova automática de teoremas** e **lógica de primeira ordem**.

Ele garante que, para uma fórmula universalmente válida, basta verificar um número finito de instâncias geradas pelo universo de Herbrand para provar sua validade. Ou seja, mesmo que o universo de possibilidades seja infinito, a prova pode ser encontrada examinando um subconjunto finito.

---

## Sobre o Script

O script `herbrand_finitude_tabela.py` gera uma tabela que mostra:

- **N**: o nível de profundidade na geração de termos de Herbrand.
- **Início (2^N)**: a quantidade mínima de termos de Herbrand até o nível N.
- **Estimado (Teorema)**: uma estimativa do número médio de termos necessários até N, calculada pela média entre o início e o fim.
- **Fim (2^(N+1)-1)**: o número máximo de termos possíveis até o nível N+1 (limite superior da soma geométrica).

A lógica da estimativa baseia-se na soma dos termos de uma progressão geométrica, pois o número de termos possíveis cresce exponencialmente com N.

### Como usar

Basta executar o script em Python 3:

```bash
python herbrand_finitude_tabela.py
````

Ele imprimirá a tabela com os valores para N de 0 a 9.

---

## Resultado esperado da tabela

| N | Início (2^N) | Estimado (Teorema) | Fim (2^(N+1)-1) |
| - | ------------ | ------------------ | --------------- |
| 0 | 1            | 1                  | 1               |
| 1 | 2            | 2                  | 3               |
| 2 | 4            | 5                  | 7               |
| 3 | 8            | 11                 | 15              |
| 4 | 16           | 23                 | 31              |
| 5 | 32           | 47                 | 63              |
| 6 | 64           | 95                 | 127             |
| 7 | 128          | 191                | 255             |
| 8 | 256          | 383                | 511             |
| 9 | 512          | 767                | 1023            |

---

## Comentários sobre o script

* O script evita o uso direto da coluna "Esperado pelo teorema", gerando a estimativa por cálculo.
* A estimativa do teorema é feita pela média entre o número mínimo (`2^N`) e o número máximo (`2^(N+1)-1`) de instâncias possíveis.
* Isso proporciona uma aproximação razoável do crescimento exponencial do universo de Herbrand.
* O script é simples, fácil de modificar para outros intervalos de N e pode ser usado como base para estudos de complexidade em provas automáticas.

---

## Possíveis extensões

* Implementar a geração real das instâncias de Herbrand.
* Calcular tempo de prova estimado em sistemas automatizados.
* Visualização gráfica do crescimento (por demanda).

---

## Referências

* Herbrand, J. (1930). Recherches sur la théorie de la démonstration.
* Enderton, H. B. (2001). A Mathematical Introduction to Logic. Academic Press.
* Logic and Automated Theorem Proving - Stanford Encyclopedia of Philosophy.

---

### Licença

Este projeto é aberto e pode ser utilizado para fins educacionais.

--- 


## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
