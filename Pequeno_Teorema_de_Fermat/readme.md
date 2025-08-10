## 🔐 **Pequeno Teorema de Fermat: Detectando Números Compostos com Python!**

### 📌 O que é o Pequeno Teorema de Fermat?

O **Pequeno Teorema de Fermat** é uma ferramenta poderosa da teoria dos números, com aplicação prática na detecção de **números primos**.

> Se **p** é um número primo e **a** é um número inteiro que não é múltiplo de **p**, então:
>
> $$
> $$

a^{p-1} \equiv 1 \ (\text{mod} \ p)
]

Ou seja, se esse resultado não for verdadeiro para algum valor de **a**, então **p não é primo**!

---

### 🔍 O que é **composto com base de Fermat**?

Um número **composto com base de Fermat** é aquele que **falha** no teste:

$$
a^{n-1} \mod n \ne 1
$$

Se isso ocorrer para alguma base `a`, o número **é certamente composto**.
✅ É uma maneira rápida de excluir candidatos a primos.

---

### ❗ O que é um **falso positivo de Fermat**?

Nem todo número que **passa** no teste de Fermat é realmente primo!
Existem **números compostos** que conseguem enganar o teste — são chamados de **falsos positivos de Fermat**.

📌 Exemplo: os **números de Carmichael**.

Por isso, o teste de Fermat é bom para detectar **compostos**, mas **não é 100% confiável** para confirmar primos.

---

### ✅ O que é um número **primo**?

Um número é **primo** quando só é divisível por 1 e por ele mesmo.

Se ele **passa no teste de Fermat com todas as bases pequenas** (como 2, 3, 5, 7) e não é Carmichael, então provavelmente **é primo**.

---

## 🧪 O script: `Pequeno_Teorema_de_Fermat.py`

Criamos um script em Python que:

* Percorre **intervalos definidos por uma tabela**
* Para cada intervalo, testa se o **número "procurado"** falha no **Pequeno Teorema de Fermat** com múltiplas bases (`2, 3, 5, 7`)
* Se falhar, **marca como COMPOSTO** e exibe sua **fatoração prima**

### 🧠 Exemplo de teste:

```bash
📌 Intervalo [32, 63] — Procurando: 49
------------------------------------------------------------
🎯 >>>>> 49 falha no teste de Fermat → COMPOSTO! | Fatores: 7^2 <<<<<
```

Ou seja, o número **49**, embora pareça inofensivo, é rapidamente detectado como composto!

---

## 📊 Resultado Final

O script percorreu os intervalos:

| Início | Procurado | Fim   |
| ------ | --------- | ----- |
| 1      | 1         | 1     |
| 2      | 3         | 3     |
| 4      | 7         | 7     |
| 8      | 8         | 15    |
| ...    | ...       | ...   |
| 8192   | 10544     | 16383 |

E encontrou diversos números compostos com sucesso, como:

* **8 = 2³**
* **21 = 3 × 7**
* **49 = 7²**
* **76 = 2² × 19**
* **224 = 2⁵ × 7**
* **10544 = 2⁴ × 659**

---

## 💡 Conclusão

✅ O Pequeno Teorema de Fermat é uma ferramenta excelente para **detectar compostos rapidamente**.
⚠️ Mas deve ser usado com **múltiplas bases** para evitar falsos positivos.

💻 O script desenvolvido mostra como usar esse teorema de forma **efetiva, automatizada e clara**, exibindo os resultados em intervalos específicos com destaque para o número procurado.

---

Se você curtiu esse projeto, podemos evoluir ele com:

* 🎨 Interface gráfica
* 📁 Exportação de resultados
* 🧠 Combinação com outros testes de primalidade

Quer ver a próxima versão? 🚀

---

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com 
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
