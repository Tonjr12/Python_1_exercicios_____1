num = int(input('digite um numero inteiro que deseja ser convertido: '))
print('''ESCOLHA UMA DAS BASES PARA CONVERSÃO:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter parq HEXADECIMAL''')

opção = int(input('Qual sua opção?'))
if opção == 1:
    print(f'O numero {num}, convertido para BINÁRIO {bin(num)[2:]}')
elif opção == 2:
    print(f' O número {num}, convertido para OCTAL {oct(num)[2:]}')
elif opção == 3:
    print(f'O numero{num}, convertido para HEXADECIMAL {hex(num)[2:]}')
else:
    print('opção invalida')


