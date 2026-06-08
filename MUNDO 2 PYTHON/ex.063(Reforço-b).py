n = int(input('digite um numero: '))
t1 = 0
t2 = 1
print(f'{t1}->{t2}', end='')
c = 3
cp = 0
while c <= n:
    t3 = t1 + t2
    print(f'->{t3}', end='')
    t1 = t2
    t2 = t3
    c += 1
    if t3 % 2 == 0:
        cp += 1
print(f': são par o total de {cp} números da sequencia de fibonacci')

