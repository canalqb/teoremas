📊 Teorema de Feller — Análise de Meios Ajustados em Intervalos Binários

Este script Python analisa e reproduz uma tabela de intervalos baseados em potências de 2, comparando a média ajustada fornecida (como o número 49 no intervalo [32, 63]) com a média teórica exata dos intervalos. Ele é fundamentado no Teorema de Feller, aplicado à convergência de médias em distribuições discretas.

--- 

## 📘 Contexto Teórico

O Teorema de Feller é uma generalização da Lei dos Grandes Números, que garante que a média de uma sequência de variáveis aleatórias independentes (mas não necessariamente identicamente distribuídas) converge, sob certas condições, para a média esperada.

Neste projeto, utilizamos essa ideia para justificar que, dentro de um intervalo binário 
[2𝑘,2𝑘+1−1] [2k,2k+1−1], a média de valores converge para um ponto representativo — chamado aqui de meio ajustado.

--- 

## 📋 Estrutura da Tabela

Cada linha da tabela contém:

Início (2^ID): limite inferior do intervalo (potência de 2)

Fim (2^(ID+1)-1): limite superior do intervalo (um antes da próxima potência de 2)

Meio (ajustado): valor representativo do intervalo (fornecido manualmente)

Média Teórica: média aritmética exata do intervalo

Desvio: diferença entre o meio ajustado e a média teórica

--- 

## ✅ Exemplo

Para o intervalo [32, 63]:

Início: 32

Fim: 63

Média Teórica: (32 + 63) // 2 = 47

Meio (ajustado): 49

Desvio: +2

--- 

## 🛠️ Requisitos

Python 3.x

pandas

Instale o pandas se necessário:

pip install pandas

--- 

## ▶️ Como Executar

Salve o script como Teorema_de_Feller.py e execute:

python Teorema_de_Feller.py


A saída será uma tabela no terminal, mostrando os valores originais e o desvio entre os meios ajustados e as médias teóricas.

--- 

## 📈 Possibilidades de Expansão

Exportar a tabela para CSV ou Excel

Gerar gráficos comparativos de desvios

Aplicar a outras distribuições além de potências de 2

Relacionar com dados empíricos de distribuições reais

--- 

## 📄 Licença

Este projeto é de domínio público, livre para fins acadêmicos, estatísticos e educacionais.

--- 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com 
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
