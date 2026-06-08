from random import randint
from time import sleep
from operator import itemgetter

# PASSO 1: Sorteio dos dados e alimentação do dicionário
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

ranking = list()

print('🎲 VALORES SORTEADOS: 🎲')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1) # Cria o efeito de delay na tela

print('-=' * 20)

# 🎯 PASSO 2: O SEGREDO DA ORDENAÇÃO
# O dicionário não se ordena sozinho. Usamos a função 'sorted'.
# key=itemgetter(1) significa que queremos ordenar pelos VALORES (os números do dado).
# reverse=True garante que vá do maior para o menor.
# IMPORTANTE: O resultado de um sorted() em dicionário vira uma LISTA cheia de TUPLAS!
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('🏆 RANKING DOS JOGADORES 🏆')
# PASSO 3: Agora é com você!
# 'ranking' virou uma lista composta. Use um laço 'for' com 'enumerate' para
# mostrar as posições (1º Lugar, 2º Lugar...) e os dados dos jogadores.
# Dica: dentro do loop, i é o índice, e p[0] será o jogador, p[1] será a nota!

for i, v in enumerate(ranking):
    print(f' {i+1}º {v[0]} com {v[1]}')
    # O terminal deve mostrar: 1º lugar: jogadorX com X pontos.
    

print('-=' * 20)