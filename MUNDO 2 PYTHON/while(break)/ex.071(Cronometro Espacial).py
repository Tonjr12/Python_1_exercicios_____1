tempo = int(input('Quanto tempo quer calcular (segundos)?: '))
sobra = tempo
unidade = 86400  # Começamos com a "nota" de 1 Dia
cont = 0

while True:
    if sobra >= unidade:
        sobra -= unidade
        cont += 1
    else:
        if cont > 0:
            # Aqui decidimos o nome da unidade para o print
            nome = ""
            if unidade == 86400:
                nome = "Dia(s)"
            elif unidade == 3600:
                nome = "Hora(s)"
            elif unidade == 60:
                nome = "Minuto(s)"
            elif unidade == 1:
                nome = "Segundo(s)"
            print(f'{cont} {nome}')

        # TROCA DE UNIDADE (Igualzinho à troca de cédula)
        if unidade == 86400:
            unidade = 3600
        elif unidade == 3600:
            unidade = 60
        elif unidade == 60:
            unidade = 1

        cont = 0
        if sobra == 0:
            break