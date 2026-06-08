numeros =list ()

while True:
    n = int(input('digite um numero: '))
    numeros.append(n)

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('deseja continuar? [S/N] ').strip().upper()[0]
    if continuar in 'N':
        break

print(f'foram diditados {len(numeros)} números.')
numeros.sort(reverse=True)
print(f'A lista ordenada de forma decrescente {numeros}.')
if 5 in numeros:
    print('O número 5 faz parte da lista e foi encontrado nas posições: ', end='')
    # O enumerate entrega o índice computacional (c) e o valor real (v) de cada gaveta
    for c, v in enumerate(numeros):
        if v == 5:
            # Se o valor for 5, mostramos a posição com o ajuste (+1)
            print(f'{c + 1}... ', end='')
    print()  # Apenas para quebrar a linha no final
else:
    print('Não foi digitado o número 5 na lista.')
