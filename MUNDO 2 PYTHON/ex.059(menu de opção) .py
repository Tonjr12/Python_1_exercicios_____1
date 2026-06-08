from time import sleep
n1 = float(input('digite um numero: '))
n2 = float(input('digite outro numero: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>> Qual é a sua opção? '))
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} = {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n1 < n2:
            print(f'{n2} é maior que {n1}')
        else:
            print(f'Os números {n1} e {n2} são iguais')
    elif opcao == 4:
        n1 = float(input('digite um numero: '))
        n2 = float(input('digite outro numero: '))
    elif opcao == 5:
        sair = True
    else:
        print('Opção invalida')
    print('=-=' * 10)
    sleep(1)

print("fim do programa")
