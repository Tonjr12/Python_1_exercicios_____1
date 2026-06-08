senha_secreta = 'tonjr123'
acesso_liberado = False
tentativas = 0
while not acesso_liberado:
    usuario = str(input('digite sua senha: '))
    tentativas += 1
    if usuario == senha_secreta:
        acesso_liberado = True
    elif tentativas == 3:
        acesso_liberado = True
if usuario != senha_secreta and tentativas == 3:
    print(f'acesso bloqueado:você atingiu o numero maximo de {tentativas}')

else:
    print('acesso liberado')








