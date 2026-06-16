from time import sleep
def contador(i, f, p):
    # Camada de segurança (Tratamento de dados)
    if p == 0: p = 1
    if p < 0: p = abs(p)  # abs() é uma função que deixa qualquer número positivo
    print('-='*30)
    print(f'{i} até {f} de {p} em {p}')
    sleep(2.5)
    print('-='*30)
    if i < f:
        while i <= f :
            print(f'{i} ',end=' ')
            sleep(0.5)
            i += p
        print('fim')
    else:
        while i >= f:
            print(f'{i} ',end=' ')
            sleep(0.5)
            i -= p
        print('fim')
#inicio do programa
contador(1, 10, 1)
contador(10, 0, 2)
print('=-'*30)
ini= int(input('Diga o inicio da contagem: '))
fim = int(input('Diga o fim da contagem: '))
passo = int(input('Diga a passo da contagem: '))
contador(ini, fim, passo)