from random import randint
computador = randint(1, 100)
acertou = False
jogadas = 0
print(' JOGO tiro ao alvo')
print('SERÁ QUE CONSEGUE ACERTAR?')
while not acertou:
    jogador = int(input('DIGITE O NÚMERO DO SEU ALVO DE 0 A 100:'))
    jogadas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('DICA:mais forte ')
        elif jogador > computador:
            print('DICA:menos forte ')
print(f'\033[31m ACERTOU!!! COM {jogadas},TIROS!!! ')





