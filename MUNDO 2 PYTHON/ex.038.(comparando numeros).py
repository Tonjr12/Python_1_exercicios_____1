num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print(f'O primeiro número é maior \033[1;31m{num1}\033[m')
elif num1 < num2:
    print(f'O segundo número é maior \033[1;32m{num2}\033[m')
else:
    print('\033[1;31mOs números são iguais\033[m')