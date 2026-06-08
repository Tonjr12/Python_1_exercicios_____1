primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
quantidade = int(input('Quantidade de termos: '))
termo = primeiro
cont = 1
total = 0 # Quantos termos no total serão mostrados
mais = quantidade # Começamos pedindo quantos  termos o usuyario quer ver

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados.')

'''Resumo: Lógica de Carregamento Progressivo (Super PA)

Sistemas modernos raramente entregam tudo de uma vez; eles perguntam se o usuário quer mais.

### 🔑 Conceitos Chave:

* **Variable Injection**: Iniciar o sistema com uma variável (`mais = quantidade`) 
  em vez de um número fixo torna o software adaptável.
* **Accumulator Logic**: `total = total + mais` é o que define o novo 
  "horizonte" que o laço interno deve alcançar.
* **Persistent State**: Variáveis como `termo` e `cont` mantêm seus valores 
  entre as execuções do laço interno, garantindo a sequência lógica.'''