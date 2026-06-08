soma = 0 # Acumulador
cont = 0 # Contador

for c in range(1, 11, 2): # Pula de 2 em 2 (SÓ PEGA ÍMPARES)
    if c % 3 == 0: # Checa se é múltiplo de 3
        soma += c
        print(soma)

        cont += 1
        print(cont)


print(f'A soma dos {cont} valores solicitados é {soma}.')