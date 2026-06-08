amigos = []
for c in range(1,4):
    amigos.append(str(input('Digite um amigo: ')))
amigos.sort()
print(amigos)
amigos.insert(0,'Amigo')
print(amigos)