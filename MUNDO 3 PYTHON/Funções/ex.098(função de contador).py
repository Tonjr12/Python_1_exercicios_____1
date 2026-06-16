def resp(a,b,p):
    for c in range(a,11):
        print(f'{c}',end=' ')
    print(' =>FIM')
    for c in range(b,0-2,-2):
        print(f'{c}',end=' ')
    print(' =>FIM')
    for c in range(n1,n2,n3):
        print(f'{c}',end=' ')
    print(' =>FIM')


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
p = (n1,n2,n3)
a = 1
b = 10
resp(a,b,p)



