somatres = 0
for c in range(1,501):
    if c % 3 == 0:
        print(c)
        somatres+= c # somaimpar= somaimpar + c
print(f'soma dos números multiplos de 3 no intervalo de 1 a 500 é: {somatres}')
