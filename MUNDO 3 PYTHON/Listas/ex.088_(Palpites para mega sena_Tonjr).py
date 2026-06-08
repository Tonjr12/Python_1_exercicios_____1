from random import randint
from time import sleep
matrix = [0,0,0,0,0,0]
jogo = int(input('Quantos jogos deseja gerar: '))
for c in range(0, jogo):

    matrix [0] = randint(0,60)
    sleep(1)
    matrix [1] = randint(0,60)
    sleep(1)
    matrix [2] = randint(0,60)
    sleep(1)
    matrix [3] = randint(0,60)
    sleep(1)
    matrix [4] = randint(0,60)
    sleep(1)
    matrix [5] = randint(0,60)
    sleep(1)
    matrix.sort()
    print(f'Jogo {c+1}: {matrix}')
