numeros = [[],[]]
for c in range(0,7):
    valor= int(input(f'Digite o {c+1} valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('*'*30)
print(numeros)
print('*'*30)
numeros[0].sort()
numeros[1].sort()
print('-'*30)
print(numeros[0])
print(numeros[1])






