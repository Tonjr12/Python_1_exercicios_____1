time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantidade de paridas  do jogador {jogador["nome"]}: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols o jogador fez na {c+1}º $partida ?: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-'*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*30)
for k, v in  enumerate (time):
    print(f'{k+1}º', end=' ')
    for d in v.values():
        print(f'{str(d):<15} ', end=' ')
    print()
print('-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! não existe jogador com {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f' No jogo {i+1} fez {g} gols ')
        print('-'*30)
print('<< ENCERRADO >>')






