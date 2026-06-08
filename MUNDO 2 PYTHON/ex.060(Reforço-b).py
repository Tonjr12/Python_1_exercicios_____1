n = int(input('digite um número: '))

s = 0
for c in range(n , 0 , -1):
    print(f'{c}',end='')
    print( ' + ' if c > 1 else ' = ', end='')
    s += c
print(s)








'''Exercício B: A Escada de Números (Soma Sucessiva)

Peça um número (ex: 5) e calcule a soma de todos os números de 1 até ele (1+2+3+4+5).

No fatorial nós multiplicamos (f *= c), aqui você vai somar (s += c).

Mostre a sequência na tela igual você fez com o fatorial: 5 + 4 + 3 + 2 + 1 = 15.'''


# Resumo: O Poder do Range e Contagens Inversas

'''O `range()` é o motor do laço `for` e possui três "marchas":

### Conceitos Chave:

* **Start, Stop, Step**: No `range(10, 0, -1)`, o 10 é onde começa, 
  o 0 é o limite (não incluso) e o -1 é o passo (decrescente)[cite: 10].
* **Loop Efficiency**: Usar a própria variável do laço (`c`) para exibir 
  valores evita a criação de contadores manuais extras dentro do bloco[cite: 10].
* **Accumulator Switch**: 
  - Fatorial = Multiplicação progressiva (`f *= c`)[cite: 8].
  - Somatório = Adição progressiva (`s += c`)[cite: 11].'''