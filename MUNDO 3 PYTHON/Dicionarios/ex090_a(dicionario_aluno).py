turma = dict()
turma['nome'] = str(input('Nome do aluno: '))

turma['media'] = float(input(f'media do aluno {turma["nome"]}: '))

if turma['media'] >= 7:
    turma['situaçao']= 'APROVADO'
elif 5 <= turma['media'] < 7:
    turma ['situaçao']= 'RECUPERAÇÃO'
else:
    turma ['situaçao']= 'REPROVADO'
print('-='*30)
for k, v in turma.items():
    print(f' - { k.capitalize()}: {v}')
