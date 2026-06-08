numeros = []

while True:
    n =(int(input('Digite um numero: ')))
    numeros.append(n)

    fim = ' '
    while fim not in 'SN':
        fim = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if fim == 'N':
        break
par = []
impar = []
for v in numeros:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'lista de numeros digitados: {numeros}')
print(f'lista de numeros digitados que são par: {par}  ')
print(f'lista de numeros digitados que são impar: {impar} ')

for c , v in enumerate(numeros):
    if v % 2 == 0:
        print(f'-> O número par {v} foi encontrado na {c + 1}ª posição.')

    else:
        print(f'-> O número ímpar {v} foi encontrado na {c + 1}ª posição.')

