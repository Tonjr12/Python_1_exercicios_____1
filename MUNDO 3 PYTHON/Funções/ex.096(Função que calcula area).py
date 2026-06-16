def area(largura, comprimento):
    a = largura * comprimento
    # Para o Python "devolver" o valor, usamos a palavra-chave 'return'
    return a
print('CONTROLE DE TERRENOS')
print('-'*30)
largura = float(input('Qual a largura da parede? '))
comprimento = float(input('Qual a altura da parede? '))
# Chamamos a função e guardamos o resultado em uma variável ou printamos direto
print(f'A AREA DE UM TERRENO {largura:.1f}x{comprimento:.1f}é um total de {area(largura, comprimento):.2f}m\u00B2:')