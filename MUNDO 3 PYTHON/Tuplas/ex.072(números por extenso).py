numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))

    if num >= 0 and num <= 20:
        print(f'O número digitado foi {numero[num]}')

        # Início do Desafio Extra: Menu de Continuação
        encerrar = ' '
        while encerrar not in 'SN':
            encerrar = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if encerrar == 'N':
            break  # Encerra o programa global

    else:
        print('Valor Inválido')