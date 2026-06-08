convidados = int(input('digite quantos convidados: '))
sobra = convidados
cont = aluguel_total = 0
unidade = 10
while True:
    if sobra >= unidade:
        sobra -= unidade
        cont += 1
    else:

        if cont > 0:
                mesa = ''
                if unidade == 10:
                    mesa = 'mesa vip'
                    aluguel = 20
                elif unidade == 4:
                    mesa = 'mesa familia'
                    aluguel = 10
                elif unidade == 1:
                    mesa = ' cadeira avulsa'
                    aluguel = 0
                aluguel = cont * aluguel
                aluguel_total += aluguel
                print(f'quantidade de mesas: {cont} {mesa} R${aluguel},')

        if unidade == 10:
            unidade = 4
        elif unidade == 4:
            unidade = 1
        cont = 0
        if sobra == 0:
            break
print(f'total do aluguel de tudo {aluguel_total}')
print({convidados})