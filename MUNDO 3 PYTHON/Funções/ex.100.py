from random import randint
from time import sleep

# 1. Função que recebe a LISTA inteira (não desempacotada)
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n) # Adiciona na lista original
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

# 2. Função que também recebe a LISTA para percorrer
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da lista {lista}, temos {soma}')

# Programa Principal
numeros = list()
sorteia(numeros) # Passamos a lista vazia, ela volta preenchida
somaPar(numeros) # Passamos a lista preenchida para somar