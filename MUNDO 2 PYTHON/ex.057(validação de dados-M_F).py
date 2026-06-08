sexo = str(input('Digite seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'FM':
    print(' codigo invalido digite apenas M ou F')
    sexo = str(input('Digite seu sexo: [M/F]: ')).strip().upper()[0]
print(f'codigo  executado com sucesso')