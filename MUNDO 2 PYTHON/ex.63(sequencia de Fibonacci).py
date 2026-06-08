n = int(input('digite um número:'))
n1 = 0
n2 = 1
print(f'\033[31m{n1}->{n2}\033[m', end='')
c = 3
while c <= n :
    n3 = n1 + n2
    print(f'\033[31m->{n3}\033[m', end='')
    n1 = n2
    n2 = n3
    c +=1

'''# Resumo: Sequência de Fibonacci e Troca de Estados

A sequência onde o próximo termo é sempre a soma dos dois anteriores.

### 🔑 Conceitos Chave:

* **Base Terms**: Os primeiros termos (0 e 1) precisam ser exibidos ou 
  tratados fora do cálculo principal do laço.
* **State Shift (Deslocamento)**: A técnica de `t1 = t2` e `t2 = t3` é o 
  que permite que o laço "ande" para frente na sequência.
* **Computational Patterns**: Fibonacci é usado em tudo, desde arte e 
  natureza até algoritmos de compressão de dados.'''