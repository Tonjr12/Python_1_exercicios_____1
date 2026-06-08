from random import randint
from time import sleep

# A tua lista de 6 posições
matrix = [0, 0, 0, 0, 0, 0]

jogo = int(input('Quantos jogos deseja gerar: '))

for c in range(0, jogo):
    # Para cada uma das 6 posições do jogo:
    for i in range(0, 6):
        while True:
            numero = randint(1, 60)  # Sorteia um número de 1 a 60

            # 🎯 O SEGREDO: Só aceita o número se ele NÃO estiver na lista
            if numero not in matrix:
                matrix[i] = numero  # Salva na posição atual
                break  # Sai do "while True" e vai para a próxima posição

    matrix.sort()  # Coloca em ordem crescente igualzinho tu fizeste!
    print(f'Jogo {c + 1}: {matrix}')

    # 🚨 IMPORTANTE: Resetar a lista para o próximo jogo não herdar os números deste!
    matrix = [0, 0, 0, 0, 0, 0]
    sleep(1)