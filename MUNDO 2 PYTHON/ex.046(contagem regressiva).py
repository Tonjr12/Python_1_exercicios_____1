from time import sleep #importei sleep da biblioteca time
'''n = int(input('Digite um numero inteiro: ')) Se quiser que a contagem comece no número 
que o usuário digitar, basta trocar o 10 por n.'''
for c in range(10, -1, -1):#menos1 porque lê ate o penultimo escrito
    print(c)
    sleep(1)
print('BUMMMMM estouro de fogos!!!')