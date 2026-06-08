salario = float(input('Qual seu salario: '))
aumento = salario + (salario * 15 /100  )
print('novo salario: R${:.2f}'.format( aumento ))