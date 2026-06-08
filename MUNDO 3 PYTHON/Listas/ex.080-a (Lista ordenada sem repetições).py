nomes = []
idades = []

for c in range(0, 3):
    nome_pessoa = str(input('Nome: '))
    idade_pessoa = int(input('Idade: '))

    # CASO 1: Se for a primeira pessoa (c == 0) ou se a idade for maior que a última da lista
    if c == 0 or idade_pessoa > idades[-1]:
        idades.append(idade_pessoa)
        nomes.append(nome_pessoa)
        print(f'{nome_pessoa} foi para o final da fila.')

    # CASO 2: Temos que usar o dedo (pos) para achar onde enfiar a pessoa mais nova!
    else:
        pos = 0  # O dedo começa apontando para a gaveta 0

        while pos < len(idades):  # Enquanto o dedo estiver na fila...

            # SE a idade da pessoa nova for MENOR ou IGUAL à idade que está na gaveta atual...
            if idade_pessoa <= idades[pos]:
                # 1. Enfie a IDADE na lista de idades na posição do dedo (pos)
                idades.insert(pos, idade_pessoa)

                # 2. Enfie o NOME na lista de nomes na MESMA posição do dedo (pos)
                nomes.insert(pos, nome_pessoa)

                print(f'{nome_pessoa} foi inserido(a) na posição {pos} da fila.')
                break  # Para o dedo e sai do while!

            pos += 1  # Se não for ali, empurra o dedo para a próxima gaveta

print('-=' * 20)
print(f'Fila de nomes organizada: {nomes}')
print(f'Fila de idades organizada: {idades}')