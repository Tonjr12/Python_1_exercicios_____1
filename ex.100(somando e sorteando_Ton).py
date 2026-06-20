from random import randint
from time import sleep

def sorteia(lista):
        for c in range(0,5):
            n = randint(0,10)
            lista.append(n)
            print(f'{n} ', end='')
            sleep(0.3)
        print()
def soma(lista):
    soma_valor = 0
    for valor in lista:
        soma_valor += valor
    print(f'{lista}, temos o valor {soma_valor} ', end='')
    sleep(0.3)





numeros = list()
sorteia(numeros)
soma(numeros)
