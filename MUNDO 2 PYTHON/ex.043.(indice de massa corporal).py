peso = float(input('digite o seu peso: '))
altura = float(input('digite sua altura: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.1f}: ', end='')
if imc < 18.5:
    print(' de 18,5	Abaixo do peso')
elif imc <= 25:
    print('18,5 a 24,9	Peso normal')
elif imc <= 30:
    print('25,0 a 29,9	Sobrepeso')
elif imc <= 40:
    print('30,0 a 34,9	Obesidade Grau I')
elif imc <= 50:
    print('35,0 a 39,9	Obesidade Grau II')
else:
    print('Maior que 40,0	Obesidade Grau III (Mórbida)')