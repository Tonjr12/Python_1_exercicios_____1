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
    print()
def somapar(lista):
    soma_par= 0
    for valor in lista:
        if valor % 2 == 0:
            soma_par += valor
    print(f'Na lista {lista} a soma dos números par são {soma_par}')
    sleep(0.3)
    print()

def somaimpar(lista):
    soma_impar = 0
    for valor in lista:
        if valor % 2 != 0:
            soma_impar += valor
    print(f'Na lista {lista} a soma dos números impar {soma_impar}')
    sleep(0.3)
    print()


numeros = list()
sorteia(numeros)
soma(numeros)
somapar(numeros)
somaimpar(numeros)
