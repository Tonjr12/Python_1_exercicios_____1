tot_gasto = cont_mil = cont_comp = mais_barato = cont_caro = cont_comp = mais_caro =0
barato = caro = ''
while True:
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    valor = float(input('Digite o valor do produto: '))
    cont_comp += 1
    tot_gasto += valor

    if valor > 1000:
        cont_mil += 1

    if cont_comp == 1:
        barato = produto
        mais_barato =  valor
        caro = produto
        mais_caro = valor
    else:

        if valor > mais_caro:
            caro = produto
            mais_caro = valor
            

        if valor < mais_barato:
            barato = produto
            mais_barato = valor

    encerrar = ' '
    while encerrar not in 'SN':
        encerrar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if encerrar == 'N':
        break


print(f' Total gasto na compra: R${tot_gasto}')
print(f' quantos produtos custam mais de R$1000 ?: {cont_mil},Produto')
print(f' produto mais barato: {barato} o valor do produto mais barato: R${mais_barato}')
print(f' produto mais caro: {caro} o valor do produto mais caro: R${mais_caro}')