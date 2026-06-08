from time import sleep

metro = float(input('>>>> Metros: '))
opcao = 0

while opcao != 5:
    print('''
    [ 1 ] Milímetros
    [ 2 ] Centímetros
    [ 3 ] Quilômetros
    [ 4 ] Digitar novo valor
    [ 5 ] Sair do programa''')

    opcao = int(input('>>>> Sua opção: '))

    if opcao == 1:
        print(f'Conversão: {metro}m = {metro * 1000}mm')
    elif opcao == 2:
        print(f'Conversão: {metro}m = {metro * 100}cm')
    elif opcao == 3:
        # Correção técnica: metros para km divide por 1000
        print(f'Conversão: {metro}m = {metro / 1000}km')
    elif opcao == 4:
        metro = float(input('Novo valor em Metros: '))
    elif opcao == 5:
        print('Finalizando', end='')
        print('.', end='', flush=True)
        print()
    else:
        print('\033[31mOpção inválida! Tente novamente.\033[m')

    print('=-=' * 15)
    sleep(1)

print('Programa finalizado com sucesso!')