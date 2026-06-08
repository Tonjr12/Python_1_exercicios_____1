primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro_termo
con = 1
while con <= 10:
    print(f'{termo}', end='')
    print(' -> ' if con <= 9 else ' ', end='')
    termo += razao
    con += 1

'''Resumo: Progressão Aritmética com While

Diferente do `range()`, aqui nós controlamos o avanço e a parada manualmente.

### 🔑 Conceitos Chave:

* **Manual Increment**: Em um `while`, se você esquecer o `cont += 1`, 
  criará um loop infinito. O contador é o freio do sistema.
* **State Persistence**: A variável `termo` guarda o valor atual e é 
  atualizada a cada volta, servindo como base para o próximo cálculo.
* **Boundary Control**: A condição `while cont <= 10` garante que o 
  sistema entregue exatamente o que foi solicitado, nem mais, nem menos.'''







