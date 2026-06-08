estoque = list()

# PASSO 1: Cadastro (Perfeito!)
while True:
    nome = str(input('Nome do produto: ').strip().upper())
    custo = float(input('Preço de custo: R$ : '))
    venda = float(input('Preço de venda: R$ : '))
    quantidade = int(input('Quantidade de Produtos: '))
    valorfinal = custo + venda
    estoque.append([nome, [custo, venda, valorfinal], quantidade])

    fim = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if fim == 'N':
        print('FINALIZANDO CADASTRO...')
        break

print('-' * 40)
print(f'{"Nº:":<4}{"PRODUTO":<15}{"QUANTIDADE":>12}')
print('-' * 40)

# PASSO 2: Listagem (Perfeito!)
for i, p in enumerate(estoque):
    print(f'{i:<4}{p[0]:<15}{p[2]:>12}')

# PASSO 3: Menu de Busca com o seu Recurso de Margem de Lucro!
while True:
    print('-' * 40)
    opc = int(input('Deseja ver qual item? (999 para finalizar): '))
    if opc == 999:
        print('FINALIZANDO SISTEMA...')
        break

    if opc <= len(estoque) - 1:
        print(f'Produto: {estoque[opc][0]}')
        print(f'-> Preço de Custo: R$ {estoque[opc][1][0]:.2f}')
        print(f'-> Preço de Venda: R$ {estoque[opc][1][1]:.2f}')
        print(f'-> Quantidade de Produtos no estoque: {estoque[opc][2]}')

        # 🎯 CORREÇÃO 1: Agora testa os dados reais do produto buscado!
        if estoque[opc][2] < 5:
            print('\033[31m⚠️🎪🎭🎭🎭🌭🩷 AVISO: Estoque crítico! O valor de oportunidade aumentou.\033[m')

            # 🎯 CORREÇÃO 2: Texto formatado limpando a rasteira da tupla
            print(f'-> Margem para a negociação: R$ {estoque[opc][1][1]:.2f} até R$ {estoque[opc][1][2]:.2f}')