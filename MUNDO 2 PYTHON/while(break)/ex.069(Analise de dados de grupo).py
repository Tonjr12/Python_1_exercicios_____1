fim =''
cont_pessoas = cont_homens = cont_mulheres = m_velha =  0
while True:
    nome = str(input('Digite seu nome: ')).strip().upper()[0:]
    sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
    idade = int(input('Digite sua idade: '))
    print('-'*30)
    if idade > 18:
        cont_pessoas += 1
    if sexo in 'F' and idade < 20:
        cont_mulheres += 1
    if sexo in 'F' and idade > 20:
        m_velha += 1
    if sexo in 'M':
        cont_homens += 1
    fim = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if fim == 'N':
        break


print(f'Foram cadastradas: {cont_pessoas} pessoas')
print(f'Foram cadastradas: {cont_homens} homens')
print(f'Foram cadastradas: {cont_mulheres} mulheres,com menos de 20 anos')
print(f'Foram cadastradas: {m_velha} mulheres,com mais de 20 anos')


'''A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''