from time import sleep
metro = float(input('>>>> Metros: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ]Converter para Milímetros.    
    [ 2 ] Converter para  Converter para Centímetros.    
    [ 3 ]  Quilômetros.    
    [ 4 ] Digitar novo valor em metros.    
    [ 5 ] Sair do programa.''')
    opcao = int(input('Você deseja converter para qual unidade de medida:? '))
    if opcao == 1:
        print(f'Conversão de {metro} em milimetro = {metro*1000},milimetros ')
    elif opcao == 2:
        print(f'Conversão de {metro} em centimetro = {metro*100},centimetros ')
    elif opcao == 3:
        print(f'Conversão de {metro} em quilometro = {metro/1000},quilometros ')
    elif opcao == 4:
        metro = float(input('Metros: '))
    elif opcao == 5:
        print(f'Saindo do programa....')
    else:
        print('Opção invalida digite novamente')

sleep(1)
print('=-='*80)
print('Programa finalizada')
print('=-='*80)












'''Peça ao usuário uma distância em Metros.

Crie um menu com as seguintes opções:



Regra de Ouro: O programa deve continuar
rodando e mostrando o menu até que o usuário escolha a opção 5.'''