frase = str(input('Digite uma frase: ')).strip().upper()
print('quantas vezes aparece a letra A aparece {}:'.format( frase.count('A')))
print('primeira vez que a letra A aparece {} :'.format (frase.find('A')+1))
print('ultima vez que a letra A aparece {}:'.format( frase.rfind('A')+1))