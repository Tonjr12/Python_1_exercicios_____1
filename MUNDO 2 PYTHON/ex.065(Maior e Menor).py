soma =  c  = maior = menor = 0
cont = 'S'
while cont == 'S':
    n = int(input('digite um numero: '))
    c += 1
    soma += n
    if c == 1:
        maior = menor = n

    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont = str(input('deseja continuar? [S/N] ')).upper().strip()[0]
if c > 0:
    media = soma / c
else :
    print('nenhum foi digitado')
print(f'a média dos numeros digitados foi {media}')
print(f'soma dos numeros digitados: {soma}')
print(f'foram digitados: {c} números')
print(f'o maior numero digitado: {maior}')
print(f'o menor numero digitado: {menor}')