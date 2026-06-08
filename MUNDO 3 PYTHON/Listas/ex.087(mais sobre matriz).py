matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = maior = scoluna=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para [{l},{c}]: '))
print('-'*40)
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c]%2==0:
            spar+=matriz[l][c]
print('-'*40)
# PASSO 2: Mostrar a matriz bem formatada na consola
for l in range(0, 3):
    for c in range(0, 3):
        # O [^5] centraliza o número em 5 espaços para ficar tudo alinhado!
        print(f'[{matriz[l][c]:^5}]', end='')
    print() # Este print vazio serve para quebrar a linha quando a coluna termina!
print(f'a soma dos valores par {spar}')
for l in range(0, 3):
    scoluna+=matriz[l][2]
print(f'A soma dos numeros da 3ª coluna é: {scoluna}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
        if matriz[1][c]>maior:
            maior = matriz[1][c]
print(f'O maior numero da 2ª linha é: {maior}')
