from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
from time import sleep
print('''Vamos jogar!''')
print('''escolha suas opções:
[ 0 ]pedra
[ 1 ]papel
[ 2 ]tesoura''')
jogador = int(input('qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print(f'computador jogou {itens[computador]}')
print(f'jogador jogou {itens[jogador]}')
print('='*30)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JPOGADA INVALIDA')






