frascos = int(input('Quantos frascos: '))
sobra = frascos
unidade = 500
cont = peso_acumulado = 0

while True:
    if sobra >= unidade:
        sobra -= unidade
        cont += 1
    else:
        if cont > 0:
            transporte = ''
            peso_unidade = 0

            if unidade == 500:
                transporte = 'Caminhão Frigorífico'
                peso_unidade = 1000
            elif unidade == 100:
                transporte = 'Caixa Térmica Grande'
                peso_unidade = 200
            elif unidade == 10:
                transporte = 'Isopor de Segurança'
                peso_unidade = 20
            elif unidade == 1:
                transporte = 'Frasco Individual'
                peso_unidade = 1

            # Calcula o peso desta etapa e soma ao total
            peso_etapa = cont * peso_unidade
            peso_acumulado += peso_etapa

            print(f'{cont} x {transporte} (Peso desta parte: {peso_etapa}kg)')

        # Troca de unidade e reset do contador
        if unidade == 500:
            unidade = 100
        elif unidade == 100:
            unidade = 10
        elif unidade == 10:
            unidade = 1

        cont = 0  # AGORA dentro do else
        if sobra == 0:  # AGORA dentro do else
            break

print('-' * 40)
print(f'CARGA COMPLETA! Peso total do comboio: {peso_acumulado}kg')