primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0 # Quantos termos no total serão mostrados
mais = 10 # Começamos pedindo 10 termos

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados.')

'''Resumo: Super PA e Laços Aninhados

Laços dentro de laços permitem criar programas que interagem continuamente com o usuário.

### 🔑 Conceitos Chave:

* **Nested Loops (Laços Aninhados)**: O `while` interno faz o trabalho repetitivo 
(mostrar termos), enquanto o externo gerencia a continuidade do sistema.
* **Cumulative Totals**: Usar uma variável `total` que acumula os novos pedidos permite 
que o contador (`cont`) saiba exatamente quando pausar novamente.
* **Flag de Encerramento**: O valor `0` é usado como uma interrupção lógica, fechando o 
programa de forma limpa quando o usuário decide parar.'''