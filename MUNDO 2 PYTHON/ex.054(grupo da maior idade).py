from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {c}ª '))
    print(f'idade: {atual - nasc}')
    if atual - nasc >= 21:
        totmaior += 1
    else:
        totmenor += 1
if totmaior > 0:
    print(f'Tem {totmaior} maiores de idade')

else:
    print(f'Tem {totmenor} menores de idade')


