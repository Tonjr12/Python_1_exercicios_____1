valor = float(input('qual o valor da casa?'))
salario = float(input('qual o seu salario?'))
anos = int(input('qual a quantidade de anos?'))
prestação = valor /(anos * 12)
if prestação <= (salario * 30 / 100):
    print(f'{salario},vai pagar R$ {prestação:.2f},emprestimo \033[1;32m aprovado!\033[m')

else:
    print(f'Com o salário de R${salario:.2f}, a parcela seria de R${prestação:.2f}.')
    print('\033[1;31mEmpréstimo NEGADO!\033[m')