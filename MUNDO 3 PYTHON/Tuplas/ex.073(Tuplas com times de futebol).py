from pip._internal import index

print('#='*30)
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo',
         'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('Os 5 primeiros colocados são :',end='')
print( times[:5])
print('#='*30)
print('Os Quatro ultimos são:',end='')
print(times[-4:])
print('#='*30)
print(times)#exibe a lista normal na ordem original
print(sorted(times))#exibe a lista organizade em ordem alfabetica
print('#='*30)
print(f'Chapecoense está na {times.index("Chapecoense") + 1}ª posição do campeonato')