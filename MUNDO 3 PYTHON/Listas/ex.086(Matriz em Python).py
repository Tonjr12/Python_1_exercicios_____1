# Inicializamos a matriz 3x3 preenchida com zeros
matriz = [[0, 0, 0,0], [0,0, 0, 0], [0,0, 0, 0],[0,0, 0, 0]]

# PASSO 1: Ler os valores e encaixar nas coordenadas certas [linha][coluna]
for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 30)

# PASSO 2: Mostrar a matriz bem formatada na consola
for l in range(0, 4):
    for c in range(0, 4):
        # O [^5] centraliza o número em 5 espaços para ficar tudo alinhado!
        print(f'[{matriz[l][c]:^5}]', end='')
    print() # Este print vazio serve para quebrar a linha quando a coluna termina!