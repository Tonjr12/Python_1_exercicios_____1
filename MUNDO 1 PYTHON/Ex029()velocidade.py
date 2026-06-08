print('A VELOCIDADE MAXIMA É DE 80 KM/H')
velocidade = float(input('Qual foi a velocidade atual?'))
if velocidade > 80:
    print('VOCÊ FOI MULTADO!')
    print('A multa vai custar R$ 7.00 por km acima do limite')
    excesso = (velocidade - 80) * 7
    print('sua velocidade em KM/H, você levou a multa no valor R$ {:.2f}'.format(excesso))
else:
    print('Você está dentro do limite de 80 KM/H')
print('Dirija swmpre com segurança')
