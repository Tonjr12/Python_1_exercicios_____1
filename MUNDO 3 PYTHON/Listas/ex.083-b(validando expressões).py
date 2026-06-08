expressão = input('digite a expressão: ')
pilha = []
for caractere in expressão:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        pilha.pop()
    else:
        pilha.append(')')
        break
if len(pilha)==0:
    print('EXPRESSÃO CORRETA')
else:
    print('EXPRESSÃO INCORRETA')