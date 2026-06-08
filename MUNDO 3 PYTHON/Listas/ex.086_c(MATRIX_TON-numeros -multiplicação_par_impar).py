matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz  [l][c] = int(input(f'Digite um valor: para [{l},{c}]: '))*l*c

   #esse vai multiplicar da mesma forma só mudou o comando de multiplicação
'''for l in range(0,3):
    for c in range(0,3):
        matriz  [l][c] = int(input(f'Digite um valor: para [{l},{c}]: '))
        matriz[l][c] = matriz [l][c] * l*c'''
print('-'*40)
print('_____FILTRANDO VALORES ______')
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            print(f'[{matriz[l][c]:^5}]',end='')
        else:
        # Colocamos o :^5 no asterisco também! Assim ele ocupa o mesmo espaço do número!
            print(f'[{"*":^5}]', end='')
    print()
print('-'*40)
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 != 0:
            print(f'[{matriz[l][c]:^5}]',end='')
        else:
        # Colocamos o :^5 no asterisco também! Assim ele ocupa o mesmo espaço do número!
            print(f'[{"*":^5}]', end='')
    print()