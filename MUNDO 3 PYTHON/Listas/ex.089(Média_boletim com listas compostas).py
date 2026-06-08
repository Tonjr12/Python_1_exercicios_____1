lista = list()

while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite 1ª a nota do aluno: '))
    nota2 = float(input('digite a 2ª a nota do aluno: '))
    media = (nota1 + nota2) / 2
    lista.append([nome,[nota1,nota2],media])
    fim = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if fim == 'N':
            break
print('-'*30)
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i,a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f} ')
while True:
    print('-'*30)
    opc = int(input('Mostrar nota de qual aluno? (999 para parar) '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(lista)-1:
        print(f'Notas{lista [opc][0]} são {lista [opc][1]}')


