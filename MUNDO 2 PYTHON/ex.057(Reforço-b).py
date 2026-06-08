idade = int(input('Digite sua idade: '))
while idade < 18 or idade > 100:
    print(f'idade: {idade}, invalido digite novamente')
    idade = int(input('Digite sua idade: '))
print(f'idade: {idade},cadastrado com sucesso')












'''Faça um programa que leia a idade de um novo motorista. 
O programa só deve aceitar idades entre 18 e 100 anos. Se ele digitar algo fora disso, mostre 
"Idade impossível! Tente de novo" e peça a digitação novamente.'''