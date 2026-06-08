maiorpeso = 0
menorpeso = 0
for p in range(1, 4):
    print('Nome: ', end='')
    nome = str(input()).strip()
    print('Peso (kg): ', end='')
    peso = float(input())
    if p == 1:
        maiorpeso = peso
        menorpeso = peso
        pesada = nome
        leve = nome
    else:
        if peso > maiorpeso:
            maiorpeso = peso
            pesada = nome
        if peso < menorpeso:
            menorpeso = peso
            leve = nome
print(f'{maiorpeso},{pesada} ')
print(f'{menorpeso},{leve}  ')




