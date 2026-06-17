from random import randint
def maior(*num):
    maior = contador = 0
    print('-'*40)
    for valor in num:
        print(f'{valor} ', end='')
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'foram informados {contador} numeros e o maior é {maior}')



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print('-'*40)
numeros_sorteados = []
for c in range(0, 6):
    numeros_sorteados.append(randint(0, 10))
maior(*numeros_sorteados)
