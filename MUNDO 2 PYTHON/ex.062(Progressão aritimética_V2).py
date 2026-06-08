primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro_termo
con = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while con <= total:
        print(f'{termo}->', end='')
        termo += razao
        con += 1
    print('pausa')
    mais = int  (input('Quantos termos deseja mostrar a mais:? '))
print(f'progressão finalizada com  {total} termos.')