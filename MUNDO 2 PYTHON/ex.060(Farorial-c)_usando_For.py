n = int(input('Digite um número para calcular seu Fatorial: '))
f = 1
print(f'Calculando {n}! = ', end='')

# O range começa no número (n), vai até o 0 (para no 1) e desce de -1 em -1
for c in range(n, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c  # Aqui a mágica acontece: f acumula a multiplicação

print(f'{f}')

''' Resumo: Fatorial e Acumuladores Progressivos

Diferente da soma (+=), o fatorial usa a multiplicação acumulada (*=).

  Conceitos Chave:

***Starting Point**: O acumulador de multiplicação (`f`) deve sempre 
  *começar em **1**. Se começar em 0, o resultado será sempre 0[cite: 8].
Step Control (`-1`)**: No `for`, o terceiro parâmetro do `range` 
  *indica que estamos contando de trás para frente.
Inline Conditionals**: O uso do `if/else` dentro do `print` (ternário) 
  *serve para trocar o "x" pelo "=" apenas na última volta do laço.'''




