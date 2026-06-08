salario = float(input('Digite o seu salario: '))
if salario > 1250:
    print('seu salario está acima de 1250 ')
    print('Por isso tera um reajuste de 10%')
    aumento = salario + (salario * 10 / 100)
else:
    print('Seu salario esta abaixo de 1250')
    print('Por isso tera um reajuste de 15%')
    aumento = salario + (salario * 15 / 100)
print('Seu novo salário será {}'.format(aumento))
