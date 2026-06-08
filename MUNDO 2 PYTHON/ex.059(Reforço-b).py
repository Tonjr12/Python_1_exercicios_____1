from time import sleep
saldo = 1000
novo_saldo = saldo
opçao = 0
while opçao != 4:
    print('''\033[32m
    [ 1 ] Ver Saldo.
    [ 2 ] Depositar .
    [ 3 ] Sacar .
    [ 4 ] Sair.
    \033[m''')
    opçao = float(input('\033[36mDigite a opção:?\033[m '))
    if opçao == 1:
        print(f'\033[32mSaldo: R$ {saldo}\033[m')
    elif opçao == 2:
        deposito = float(input('\033[34mDigite o valor do deposito:\033[m '))
        if deposito <= 0:
            print('deposito invalido')
        elif deposito > 0:
            saldo += deposito
    elif opçao == 3:
        saque = float(input('\033[31mDigite o valor do saque: \033[m'))
        if saque > saldo:
            print('\033[31m>>>>>Saldo insuficiente\033[m')
        elif saque <= saldo:
            saldo -= saque
    elif opçao == 4:
        print('\033[31mFinalizando', end='')
        for _ in range(3):
            sleep(0.5)
            print('.', end='', flush=True)
        print()
    else:
        print('\033[31mOpção inválida! Tente novamente.\033[m')

        print('=-=' * 15)
        sleep(1)

import time
import os


def animacao_final():
    # Cores ANSI
    AMARELO = '\033[1;33m'
    VERMELHO_NEON = '\033[1;91m'
    RESET = '\033[0m'
    NEGRITO = '\033[1m'

    print(f'{NEGRITO}Programa finalizado com sucesso!{RESET}')
    print('=-=' * 15)

    try:
        # Loop para o efeito de piscar (roda 6 vezes, ~3 segundos)
        for i in range(6):
            # Alterna a cor entre amarelo e vermelho a cada ciclo
            cor = AMARELO if i % 2 == 0 else VERMELHO_NEON

            # \r faz o cursor voltar para o início da linha para sobrescrever
            # end='' impede que o print pule uma linha automaticamente
            print(f'\rOBRIGADO POR UTILIZAR O CAIXA ELETRÔNICO DO {cor}TON{RESET}{cor}!!!{RESET}', end='', flush=True)

            time.sleep(0.5)

        # Finaliza a linha após o loop
        print('\n' + '=-=' * 15)

    except KeyboardInterrupt:
        pass


animacao_final()











'''Comece com uma variável saldo = 1000.
Mostre um menu com as opções:
[ 1 ] Ver Saldo.
[ 2 ] Depositar (peça o valor e some ao saldo).
[ 3 ] Sacar (peça o valor e subtraia do saldo).
[ 4 ] Sair.
Desafio de Arquiteto:
Se o usuário tentar sacar mais do que tem, exiba: "Saldo Insuficiente".
Não aceite depósitos ou saques de valores negativos.'''