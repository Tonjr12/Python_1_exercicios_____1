print('CUSTO DO VALOR DA VIAGEM:' )
print('Até 200 KM,R$ 0.50')
print('Acima de 200 KM,R$ 0.45 ')
distancia = float(input('Qual a distancia da viagem em km: '))
if distancia <= 200:
    preço = distancia * 0.50
    print('o valor da sua viagem é R$ {:.2f}'.format(preço))
else:
    preço = distancia * 0.45
    print('O valor da sua viagem é R$ {:.2f}'.format(preço))