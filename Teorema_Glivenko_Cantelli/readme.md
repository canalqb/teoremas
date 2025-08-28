📚 O Teorema de Glivenko-Cantelli

Imagine lançar uma moeda mil vezes. Você não saberá o resultado de cada lançamento,  
mas, com o tempo, verá um padrão emergir: a frequência de caras e coroas tende a se estabilizar.  
Agora, imagine isso acontecendo não com moedas, mas com **qualquer distribuição de probabilidade**.

O Teorema de Glivenko-Cantelli nos diz exatamente isso:  
**à medida que aumentamos o tamanho de uma amostra aleatória, a distribuição empírica**  
(construída a partir dos dados observados) **converge uniformemente** para a distribuição teórica.

Ou, poeticamente:  
> “Com paciência suficiente, o mundo observável se curva à ordem invisível da teoria.”

✨ O que este script faz?

Este script é um experimento visual e numérico inspirado nesse teorema.

Para diferentes valores de `A`, geramos amostras aleatórias de tamanho `n = 2^(A+1) - 1`  
da distribuição normal padrão. Depois, comparamos a **CDF empírica** (acumulada dos dados)  
com a **CDF teórica** (da normal padrão).

Queremos encontrar **o ponto de maior diferença** entre essas duas curvas —  
aquele exato valor onde a teoria e a prática mais discordam.

Esse ponto (x) é então mapeado para o intervalo inteiro `[2^A, 2^(A+1) - 1]`  
resultando em um número curioso chamado aqui de **‘PROCURANDO’**.

📊 Saída esperada

C:\Users\Notebook\Desktop\teoremas>Glivenko_Cantelli

2^A        PROCURANDO      2^(A+1)-1  
1          '1              1  
2          '3              3  
4          '5              7  
8          '10             15  
16         '29             31  
32         '57             63  
64         '101            127  
128        '184            255  
256        '438            511  
512        '785            1023  
1024       '1586           2047  
2048       '2479           4095  
4096       '6905           8191  

Cada linha representa uma busca:  
quanto mais dados, mais perto estamos da verdade — e mais longe da surpresa.

🔍 Extras curiosos

Você também encontrará uma pequena brincadeira no final do código:  
dada uma posição desejada dentro de um intervalo, qual seria o valor de `x` na normal  
que o geraria? Isso é feito invertendo a CDF com a função `ppf`.

Exemplo:  
x que gera '21' no intervalo [16, 31] = -0.1257  
x que gera '49' no intervalo [32, 63] = 0.4602  

Pequenos mapas de volta ao centro da curva.

⚙️ Como usar

1. Salve o código como `glivenko_cantelli.py`  
2. Certifique-se de ter Python 3 e os pacotes `numpy` e `scipy` instalados  
3. Execute no terminal com:

   > python glivenko_cantelli.py

💡 Requisitos

- Python 3.x  
- NumPy  
- SciPy  

🌌 Por quê?

Porque a matemática tem algo de místico.  
Porque os dados falam, mas a teoria sussurra por trás deles.  
E porque, às vezes, tudo que queremos é ver a ordem emergir do caos —  
linha por linha, número por número.

---

Glivenko. Cantelli. Dois nomes.  
Um lembrete eterno de que com o tempo, tudo se revela.


---  
 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
