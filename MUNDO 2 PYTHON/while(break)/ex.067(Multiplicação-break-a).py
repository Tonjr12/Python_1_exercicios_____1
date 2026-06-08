n = 0
c = 1
while True:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))
    if n1  < 0 or n2 < 0:
        break
    print(f'{n1} x {n2} = {n1 * n2}')
print('fim')