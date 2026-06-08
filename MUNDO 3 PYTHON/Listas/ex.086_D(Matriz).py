#from random import randint
matriz = [[0,0,0],[0,0,0],[0,0,0]]
cont = 1
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = cont
        cont += 1
        print(f'[{matriz[l][c]:^5}]', end='')

