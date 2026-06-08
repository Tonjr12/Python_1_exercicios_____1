n = int(input('digite um numero para saber se é primo: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c} \033[m', end=' ')
if tot == 2:
    print(f' O número: {n}, é primo!')
else:
    print(f'O numero {n}, não é primo!')
print(f'\033[mo numero {n}, é divisivel, {tot},vezes')
