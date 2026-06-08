l1 = float(input('Digite o valor da primeira lado : '))
l2 = float(input('Digite o valor da segunda lado : '))
l3 = float(input('Digite o valor da terceira lado : '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('é triângulo')
else:
    print('não é triangulo')