from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: ')).strip().capitalize()
ano_nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - ano_nasc
dados['CTPS'] = int(input('Carteira de trabalho:(0: nao tem) '))
print('-'*30)
if dados['CTPS'] != 0:
   dados['contratação']= int(input('Ano de contratação: '))
   dados['salario']= float(input('Salario: '))
   # Lógica correta:
   # 1. (dados['contratação'] - ano_nascimento) = Idade na contratação
   # 2. + 35 = Idade quando completar 35 anos de contribuição
   idade_na_contratacao = dados['contratação'] - ano_nasc
   dados['idade_aposentadoria'] = (dados['contratação'] - ano_nasc) + 35
print('-=' * 20)
for k, v in dados.items():
    # Capitalize para deixar a chave bonitinha, e formatamos apenas o salario se ele existir
    if k == 'salario':
        print(f' - {k.capitalize()} tem o valor de R$ {v:.2f}')
    else:
        print(f' - {k.capitalize()} tem o valor {v}')