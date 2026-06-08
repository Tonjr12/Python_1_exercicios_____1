temporario = list()
principal = list()
maior = menor = cont = 0
while True:
    temporario.append(str(input('Digite um nome: ')))
    temporario.append(float(input('Digite um peso: ')))
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-'*30)
print(f'os dados gerados foram {principal}')
print(f'Foram cadastradas: {len(principal)} pessoas')

print('-'*30)
print(f'O maior peso foi de {maior} Kg')
print(f'O menor peso foi de {menor} Kg')

