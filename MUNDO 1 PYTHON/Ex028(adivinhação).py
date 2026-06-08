from random import randint
from time import sleep
computador = randint(0, 5)
'''print(computador)'''
print('-=-' * 50)
print('Vou pensar em um numero entre 0 e 5 tente adivinhar...')
print('-=-' * 50)
jogador = int(input('qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Você acertou!')
else:
    print('Você perdeu! pensei no numero: {}!! e você tentou o número: {}!!'.format(computador, jogador))


