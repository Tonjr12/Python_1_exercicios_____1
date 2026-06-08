expressao = str(input('Digite a expressão matemática: '))
pilha = []

for caractere in expressao:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        # Se a pilha não estiver vazia, removemos o parênteses aberto correspondente
        if len(pilha) > 0:
            pilha.pop()
        else:
            # Se a pilha estiver vazia e achamos um ")", a expressão já está errada!
            pilha.append(')')
            break

print('-=' * 20)
# Se a pilha terminou vazia, significa que tudo o que abriu, fechou perfeitamente!
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')