nome = str(input('Digite seu nome:'))
print('seu nome todo maiscúlo {}'.format(nome.upper()))
print('seu nome em minusculo {}'.format(nome.lower()))
print('seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separar = nome.split()
print('seu primeiro nome {} tem {} letras'.format(separar[0], len(separar[0])))

