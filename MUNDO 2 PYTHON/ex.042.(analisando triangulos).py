l1 = int(input('digite o primeiro seguimento: ').strip())
l2 = int(input('digite o segundo seguimento: ').strip())
l3 = int(input('digite o terceiro seguimento: ').strip())
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(' Triangulo ' ,end='')
    if l1== l2 == l3:
        print('Equilatero')
    elif l1 != l2 != l3 != l1 :
        print('Escaleno')
    else:
        print('Esoceles')
else:
    print('Não é triangulo')



