primeiro = int(input('Primeiro termo: '))
razao = int(input('digite a razão'))
decimo = primeiro + (10 - 1) * razao#formula decimo numero de uma PA
print(decimo)
for c in range(primeiro, decimo+razao,razao):
    print(c, end='->')
print('FIM')







