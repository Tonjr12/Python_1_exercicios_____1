saque = int(input('Digite o valor do saque: '))
valor = saque
cedula = 50
cont = 0
while True:
    if valor >= cedula:
        valor -= cedula
        cont += 1
    else:
        if cont > 0:
            print(f'total de cedulas: {cont} de R$ {cedula}')
        if cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 5

        elif cedula == 5:
            cedula = 1
        cont = 0
        if valor == 0:
            break












