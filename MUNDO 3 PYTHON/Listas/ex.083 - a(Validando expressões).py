expressão = input('digite a expressao: ')
pilha = []
for caracter in expressão:
    if caracter == '(' :
        pilha.append('(')
    elif caracter == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('expressão correta')
else:
    print('expressão errada')

