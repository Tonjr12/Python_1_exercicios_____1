from operator import itemgetter
sistema_vendas = {
    'Tonjr':15800,
    'Isaac':13000,
    'Fatima':90000,
    'Carol':88899
}
ordenacoes = []
for k, v in sistema_vendas.items():
    print(f'{k} tirou {v}')
ordenacoes = sorted(sistema_vendas.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ordenacoes):
    print(f'{i+1}º - {v[0]} - {v[1]}')