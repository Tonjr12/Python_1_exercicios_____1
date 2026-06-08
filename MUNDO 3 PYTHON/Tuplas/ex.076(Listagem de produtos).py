listagem = ('lapis',1.75,
            'borracha',2.00,
            'apontador',4.00,
            'caderno',5.00,
            'estojo',9.00,
            'caneta',3.49,
            'muchila',25.00,
            'livro',50.00,
            'compasso',15.50)
# Cabeçalho decorativo bonito
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        # Mostra o produto alinhado à esquerda com pontinhos, sem pular linha (end='')
        print(f'{listagem[pos]:.<30}', end='')
    else:
        # Mostra o R$ e o preço alinhado à direita com 2 casas decimais
        print(f'R$ {listagem[pos]:>6.2f}')

print('-' * 40)
