from datetime import date
atual = date.today().year
ano= int(input('Digite o ano de nascimento  do atleta: '))
idade = atual - ano
print(f'O atleta tem {idade} anos.')

# Começamos a classificação
print('Classificação: ', end='') # O end='' serve para não pular linha
if   idade <= 9:
    print(f'O atleta tem {idade} anos.\033[31mMIRIM\033[m')
elif idade <= 14:
    print(f'O atlets tem {idade} anos.\033[31mINFANTIL\033[m')
elif idade <= 19:
    print(f'O atleta tem {idade} anos.\033[31mJUNIOR\033[m')
elif idade <= 25:
    print(f'O atleta tem {idade} anos.\033[31mJUNIOR\033[m ')
else:
    print(f'O atleta tem {idade} anos.\033[31mMASTER\033[m')

