garrafas = int(input('Digite a quantidade de garrafas: '))
caixa = garrafas
unidade = 24
cont = 0
while True:
    if caixa >= unidade:
        caixa -= unidade
        cont+=1
    else:
        if cont > 0:
            engradado = ''
            if unidade == 24 :
                engradado = 'Caixa G'
            elif unidade == 6 :
                engradado = 'Caixa M'
            elif unidade == 1 :
                engradado = 'Avulso'
            print(f'{cont} {engradado}')
        if unidade == 24:
            unidade = 6
        elif unidade == 6:
            unidade = 1
        cont = 0
        if caixa == 0 :
            break











'''Engradado
G: cabe
24
garrafas.

Engradado
M: cabe
6
garrafas.

Unidade: 1
garrafa
avulsa.'''