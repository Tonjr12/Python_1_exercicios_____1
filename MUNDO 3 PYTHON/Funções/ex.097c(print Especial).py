def escreva(msg):
    tam = len(msg) + 4 # O +4 dá um espaçamento elegante nas laterais
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

# Agora a função é independente!
# Ela funciona com qualquer texto, a qualquer momento.
escreva('Tonjr Desenvolvedor')
escreva('Curso em Vídeo')   