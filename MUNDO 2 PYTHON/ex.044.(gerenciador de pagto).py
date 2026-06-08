nome = 'TONJR'
print(f'{nome:*^80}')
valor = float(input('Digite um valor: '))
print('''FORMAS DE PAGTO
[ 1 ] Á vista dinheiro ou cheque( desconto 10%)
[ 2 ] á vista cartão( desconto 5%)
[ 3 ] 2x cartão(sem desconto)
[ 4 ] 3x ou mais no cartão(20% de juros''')
opcao = int(input('digite sua opcao: '))
if opcao == 1:
    vista = valor - (valor * 10 / 100)
elif opcao == 2:
    vista = valor - (valor * 5 / 100)
elif opcao == 3:
    vista = valor
    parcela = vista / 2
    print(f'o valor da sua parcela será de  2x R$ {parcela:.2f}')
elif opcao == 4:
    quantidade = int(input('digite quantas parcelas: '))
    vista = valor + (valor * 20 / 100)
    parcela = vista / quantidade
    print(f'O valor da sua parcela será {quantidade} x  de R$ {parcela:.2f}')
else:
    vista = 0
    print('\033[31m opcao invalida\033[m')
if vista > 0:
    print(f'O valor da sua compra foi de R$ {valor:.2f} e o pagamento foi de R$ {vista:.2f},valor final ')

