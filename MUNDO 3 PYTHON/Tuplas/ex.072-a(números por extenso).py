numero = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:

    num = int(input('digite um numero entre 0 e 20: '))

    if 0 <= num <= 20:

        print(f'o numero digitado foi {numero[num ]}')

        encerrar = ' '

        while encerrar not in 'SN':

            encerrar = str(input('deseja continuar? [S/N] ')).strip().upper()

        if encerrar in 'Nn':

                break



