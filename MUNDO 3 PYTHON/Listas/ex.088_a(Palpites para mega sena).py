from random import randint
from time import sleep
lista = list()
jogos = list()
total = 1
quantidade = int(input('quantos jogos quer gerar: '))
while total <= quantidade:
    cont = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for i , lista in enumerate(jogos):
    print(f'Jogo {i+1}: {lista}')
    sleep(1)




