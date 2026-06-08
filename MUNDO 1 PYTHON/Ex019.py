'''aqui importei o random que puxei dentro da caixa o choice'''
'''import random
n1 = str(input("digite o primeiro nome: "))
n2 = str(input("digite o segundo nome: "))
n3 = str(input('digite o terceiro nome: '))
n4 = str(input('digite o quarto nome: '))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))'''

'''ja aqui somente puxedi da caixa o choice'''


from random import choice
n1 = str(input("digite o primeiro nome: "))
n2 = str(input("digite o segundo nome: "))
n3 = str(input('digite o terceiro nome: '))
n4 = str(input('digite o quarto nome: '))
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))



