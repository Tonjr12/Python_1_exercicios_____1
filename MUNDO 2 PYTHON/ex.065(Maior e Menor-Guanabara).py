# Inicialização zerada - O Arquiteto prepara o terreno
soma = quant = maior = menor = 0
continuar = 'S'

while continuar == 'S':
    n = int(input('Digite um número inteiro: '))
    soma += n
    quant += 1

    # Lógica do Primeiro Round (Referência Inicial)
    if quant == 1:
        maior = menor = n
    else:
        # Comparações de extremos
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    # O "Vigia" pergunta se a obra continua
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

# Resultados Finais
if quant > 0:
    media = soma / quant
    print(f'Você digitou {quant} números e a média foi {media:.2f}')
    print(f'O maior valor foi {maior} e o menor foi {menor}')
else:
    print('Nenhum valor foi processado.')