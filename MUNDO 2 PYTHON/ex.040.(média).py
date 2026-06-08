nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Aluno reprovado!{media:.2f}')
elif  7 > media >= 5: # média é maior ou igual a 5 e menor que 7
    print(f'Aluno em recuperação! {media:.2f}')
else:
    print(f'Aluno aprovado! {media:.2f}')