pessoa = dict()
galera = list()
media = soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in  'SN':
            break
        print('ERRO! Responda apenas Sim ou Não' )
    if  resp == 'N':
        break
print('-'*30)
print('galera'.center(30))
print('-'*30)
print(galera )
print(f'A) O galera tem {len(galera)} pessoas.')
media = soma / len(galera)
print(f'B) a média de idades é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]}', end=' ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('>>ENCERRADO<<')
