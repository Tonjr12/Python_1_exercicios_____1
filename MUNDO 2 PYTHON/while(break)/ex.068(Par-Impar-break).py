from random import randint
vitorias = 0
while True:
    jogador = int(input('Digite um numero: (0,10):'))
    computador = randint(0,10)
    soma = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar:')).upper().strip()[0]
    print(f'jogador {jogador}, computador {computador}, jogada {soma}')
    print('-'*30)
    print(f'Deu Par' if soma % 2 == 0 else 'Deu impar')
    if escolha == 'P':
        if  soma % 2 == 0:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')

    print(f'GAME OVER! Você venceu {vitorias} vezes.')
print(f'GAME OVER! Você venceu {vitorias} vezes consecutivas.')



