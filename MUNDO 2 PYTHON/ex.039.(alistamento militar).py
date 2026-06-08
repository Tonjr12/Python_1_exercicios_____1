from datetime import date
atual = date.today().year
sexo = input('Qual seu sexo? [M/F] ').upper().strip()
if sexo == 'F':
    print('Não é permitido o alistamento para mulheres')
elif sexo == 'M':
    anonascimento = int(input('Digite o ano de nascimento: ').strip())
    idade = atual - anonascimento
    print(f'você tem {idade} anos de idade')
    if idade == 18:
        print('\033[31m SE ALISTE IMEDIATAMENTO MILITAR \033[m')
    elif idade < 18:
        saldo = 18 - idade
        ano_alistamento = atual + saldo
        print(f'Sua idade é: {idade}')
        print(f' Alistamento militar no ano{ano_alistamento}')
    else:
        saldo = idade - 18
        ano_alistamento = atual - saldo
        print(f'Você deveria ter se alistado há {saldo} anos atrás. O ano do alistamento foi: {ano_alistamento}')
        print(f'No ano de {ano_alistamento}')
