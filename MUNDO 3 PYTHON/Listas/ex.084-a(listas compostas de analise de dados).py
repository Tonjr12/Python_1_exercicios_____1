temp = []
prin = []
maior = menor = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('peso:')))

    if len(prin)==0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    prin.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-'*30)
print(f'{len(prin)} pessoas cadastrada(s)')
print(f'maior peso de {maior} Kg. peso de:', end=' ')
for p in prin:
    if p[1] == maior:
        print(f',{p[0]}', end=' ')
print()
print('-'*30)
print(f'menor peso de {menor} Kg.peso de:', end=' ')
for p in prin:
    if p[1] == menor:
        print(f',{p[0]}', end=' ')
print()

