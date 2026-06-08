totidade = 0
mais_velho = 0
mais_novas = 0
nome_velho = ''
for c in range(1,5):
    print(f'Primeira pessoa {c}ª')
    nome = str(input('Digite seu nome: ')).strip()
    sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()
    idade = int(input('Digite sua idade: '))
    totidade += idade
    #para definir o mais velho
    if c == 1 and sexo == 'M':
        mais_velho = idade
        nome_velho = nome
    if idade > mais_velho and sexo == 'M':
        mais_velho = idade
        nome_velho = nome
    #para definir a mulher mais nova
    if  sexo == 'F' and idade < 20:
        mais_novas += 1

media = totidade / 4
print(f'A média de idade do grupo{media:.2f} anos')
print(f'O homen mais velho é {nome}e tem {mais_velho} anos ')
print(f'tem {mais_novas} mulheres com menos de 20 anos')



