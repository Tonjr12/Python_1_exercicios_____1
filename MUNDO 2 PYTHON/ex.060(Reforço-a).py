'''from time import sleep
n = int(input('digite um número: '))
print(f'{n}...',end='')
sleep(1)
while n > 0:

    n -=1
    print(f'{n}',end='')
    sleep(0.5)
    print('...' if n > 0 else ' >>>>>> ', end='')
    sleep(1)
print('BUMMMMMMMM!!!!')'''


from time import sleep
n = int(input('digite um número: '))
c = n
print(f'{n}...',end='')

sleep(1)
for  c in range (c , 0,-1):

    n -=1
    print(f'{n}',end='')
    sleep(0.5)
    print('...' if n > 0 else ' >>>>>> ', end='')
    sleep(1)
print('BUMMMMMMMM!!!!')







'''Exercício A: O Contador Regressivo Explosivo

Peça um número ao usuário e faça uma contagem regressiva até 0.

A cada segundo (sleep), mostre o número.

No final, em vez de mostrar o fatorial, mostre a frase: "BUM! EXPLOSÃO!".

Dica de Arquiteto: Use o for com o range negativo que você aprendeu agora'''