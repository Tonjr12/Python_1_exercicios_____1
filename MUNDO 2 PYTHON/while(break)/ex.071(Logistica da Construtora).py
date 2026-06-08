carga = int(input('digite qual a carga a ser transportada em toneladas: '))
caminhao = carga
unidade = 15
cont = 0
totviagem = 0
while True :
    if carga >= unidade:
        carga -= unidade
        cont += 1
        totviagem += 1
    else:
        if  cont > 0 :
            caminhao = ''
            if unidade == 15:
                caminhao = 'caminhao Bruto'
            elif unidade == 5:
                caminhao = 'caminhao Forte'
            elif unidade == 1:
                caminhao = 'caminhao Ágil'
            print(f'{cont} viagem {caminhao}. ')

        if unidade == 15:
            unidade = 5
        elif unidade == 5:
            unidade = 1
        cont = 0

        if carga == 0 :
            break
print(f'total de viagem: {totviagem}')



