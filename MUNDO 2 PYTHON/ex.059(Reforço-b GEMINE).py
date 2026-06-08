from time import sleep
from datetime import datetime  # Importamos o módulo de tempo real
import sys

# Variáveis Iniciais
saldo = 1000
extrato = []  # Lista para guardar o histórico[cite: 1]
opcao = 0

while opcao != 5:
    print('\033[32m' + '=-=' * 15)
    print('''    [ 1 ] Ver Saldo.
    [ 2 ] Depositar.
    [ 3 ] Sacar.
    [ 4 ] Ver Extrato.
    [ 5 ] Sair.''')
    print('=-=' * 15 + '\033[m')

    try:
        opcao = int(input('\033[36mDigite a opção: \033[m'))
    except ValueError:
        print('\033[31mErro: Digite um número inteiro!\033[m')
        continue

    if opcao == 1:
        print(f'\033[32mSaldo Atual: R$ {saldo:.2f}\033[m')

    elif opcao == 2:
        deposito = float(input('\033[34mValor do depósito: R$ \033[m'))
        if deposito > 0:
            saldo += deposito
            # Captura data e hora formatada
            agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            extrato.append(f"[{agora}] Depósito: + R$ {deposito:.2f}")  # Salva com data[cite: 1]
            print('\033[32mDepósito realizado!\033[m')
        else:
            print('\033[31mValor inválido!\033[m')

    elif opcao == 3:
        saque = float(input('\033[31mValor do saque: R$ \033[m'))
        if 0 < saque <= saldo:
            saldo -= saque
            # Captura data e hora formatada
            agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            extrato.append(f"[{agora}] Saque:    - R$ {saque:.2f}")  # Salva com data[cite: 1]
            print('\033[32mSaque realizado!\033[m')
        elif saque > saldo:
            print('\033[1;31mSALDO INSUFICIENTE!\033[m')
        else:
            print('\033[31mValor inválido!\033[m')

    elif opcao == 4:
        print('\033[35m' + '===' * 10 + ' EXTRATO ' + '===' * 10)
        if not extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for item in extrato:
                print(item)
        print(f"\nSaldo Final: R$ {saldo:.2f}")
        print('===' * 23 + '\033[m')

    elif opcao == 5:
        print('\033[31mFinalizando', end='')
        for _ in range(3):
            sleep(0.5)
            print('.', end='', flush=True)
        print('\033[m\n')

    else:
        print('\033[31mOpção inválida!\033[m')

    sleep(1)

# --- ANIMAÇÃO FINAL DO TON ---
AMARELO, VERMELHO, RESET = '\033[1;33m', '\033[1;91m', '\033[0m'
print(f'\033[1mPrograma finalizado com sucesso!{RESET}\n' + '=-=' * 15)

for i in range(10):
    cor = AMARELO if i % 2 == 0 else VERMELHO
    print(f'\rOBRIGADO POR UTILIZAR O CAIXA ELETRÔNICO DO {cor}TON{RESET}{cor}!!!{RESET}', end='', flush=True)
    sleep(0.5)
print('\n' + '=-=' * 15)