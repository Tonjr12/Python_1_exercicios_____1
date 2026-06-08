num = (int(input('digite um numero:')),int(input('digite um numero:')),int(input('digite um numero:')),int(input('digite um numero:')))

print(f'Os valores digitados foram: {num}')
if 9 in num:
    print(f'O numero 9 apareceu {num.count(9)} vezes')
else:
    print('o numero 9 não foi digitado')
if 3 in num:
    print(f'O numero 3 apareceu {num.index(3)+1} posição')
else:
    print('O numero 3 não foi digitado')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')
else:
    print('Não foi digitado nenhum numero par')