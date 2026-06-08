pacotes = int(input('Quantos pacotes: '))
sobra = pacotes
unidade = 100
cont = segurotot = 0
while True:
    if sobra >= unidade:
        sobra -= unidade
        cont += 1
    else:
        if cont > 0 :
            contentor = ''
            segurounidade = 0
            if unidade == 100:
                contentor = 'contentor G'
                pacote = 100
                segurounidade = 50
            elif unidade == 20 :
                contentor = 'contentor M'
                pacote = 20
                segurounidade = 15
            elif unidade == 1 :
                contentor = 'caixa individual'
                pacote = 1
                segurounidade = 2

            pacote = cont * pacote
            seguro = cont * segurounidade
            segurotot = segurotot + seguro


            print(f' {cont}  {contentor}/ pacote: {pacote} seguro R$: {seguro}')
            cont = 0
        if unidade == 100 :
            unidade = 20
        elif unidade == 20 :
            unidade = 1
        if sobra == 0 :
            unidade = 20
            break
print(f'total de pacotes: {pacotes}, seguro total da carga:{segurotot}')