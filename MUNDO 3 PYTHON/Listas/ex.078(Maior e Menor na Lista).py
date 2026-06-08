numeros = []
for c in range(0,5):
    numeros.append(int(input('Digite um numero: ')))
    print(numeros[c])
    if(c == 0):
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print(f'\033[1;31m{maior} eh o maior\033[m,\033[1;33m{menor} eh o menor\033[m')
print('#*'*30)
print(f'\033[1;34m{numeros}\033[m')
for c , v in enumerate(numeros):
    if v == maior:
        print(f'\033[1;32m Na posição {c+1} encontrei {v}, que é o maior número\033[m')
        #coloquei o c + 1 só para sair do 0 e mostrar que está na posição 1
    if v == menor:
        print(f'\033[1;31m Na posição {c+1} encontrei {v}, que é o menor número\033[m')
        # coloquei o c + 1 só para sair do 1 e mostrar que está na posição 2
print('FIM')


