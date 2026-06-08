turma = dict()

# Passo 1: Leitura dos dados
turma['nome'] = str(input('Digite o nome do aluno: ')).strip()
turma['nota1'] = float(input('Digite a primeira nota: '))
turma['nota2'] = float(input('Digite a segunda nota: '))

# Passo 2: Cálculo da Média
turma['media'] = (turma['nota1'] + turma['nota2']) / 2

# Passo 3: Validação da Situação (Correção da chave oculta!)
if turma['media'] >= 7.0:
    turma['situacao'] = 'Aprovado'
elif 5.0 <= turma['media'] < 7.0:
    turma['situacao'] = 'Recuperação'
else:
    turma['situacao'] = 'Reprovado'

print('-' * 40)
print(f'Dicionário bruto: {turma}')
print('-' * 40)

# Passo 4: Exibição elegante usando o laço que você treinou!
for k, v in turma.items():
    print(f' - {k.capitalize()} é igual a {v}')