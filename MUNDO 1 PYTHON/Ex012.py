valor = float(input('Qual o valor do produto? R$'))
novo = valor - (valor * 5/100)
print('novo valor: R${:.1f}'.format(novo))