numeros = []
while True:
    n = int(input('Digite um numero: '))

    if  n not in numeros:
        numeros.append(n)
    else:
        print('numero ja existe')

    fim = ' '
    while fim not in 'SN':
        fim = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if fim == 'N':
        break

numeros.sort()
print(numeros)



