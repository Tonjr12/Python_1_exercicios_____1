'''aqui importei a caixa de ferramnetas ramdon(tudo que é aleatorio)'''
'''import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('a ordem sera {}'.format(lista))'''


'''aqui importei a caixa de ferramenta randon(somente o shuffle)'''
from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('a ordem sera {}'.format(lista))