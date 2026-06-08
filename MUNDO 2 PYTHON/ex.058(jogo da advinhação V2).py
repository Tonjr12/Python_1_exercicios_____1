from random import randint
computador = randint(0, 10)
print('sou seu computador e vou pensar em um número entre 0 e 10')
print('será que você consegue advinhar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('qual sua jogada? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('errou mais')
        elif jogador > computador:
            print('errou menos')


print(f'acertou,foram necessarias {palpite } palpites')

