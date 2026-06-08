# n recebe o INTEIRO da ENTRADA ('Digite um numero...')
n = int(input('Digite um numero que quer ver a tabuada: '))

# n2 recebe o INTEIRO da ENTRADA ('Digite um numero até onde...')
n2 = int(input('Digite um numero até aonde quer ver a tabuada: '))

# PARA cada c DENTRO DO INTERVALO de 1 até n2:
for c in range(1, n2):
    # EXIBA o resultado da multiplicação
    print(f'{n} x {c} = {n*c}')