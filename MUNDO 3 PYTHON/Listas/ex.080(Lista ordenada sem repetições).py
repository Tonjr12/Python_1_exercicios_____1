lista = list()
for c in range(0, 5):
    n = (int(input('Digite um valor: ')))

    # CASO 1: Se for a primeira carta (c == 0) ou se for maior que a última (n > lista[-1])
    if c == 0 or n > lista[-1]:
        lista.append(n)  # Vai direto para o final da lista!
        print('Adicionado ao final da lista')

    # CASO 2: Se o número tiver que ser enfiado no meio ou no começo
    else:
        pos = 0  # Começamos a olhar a lista a partir do índice 0
        while pos < len(lista):  # Enquanto não olharmos todas as cartas da mão...
            if n <= lista[pos]:  # O número digitado é menor ou igual ao da gaveta atual?
                lista.insert(pos, n)  # Coloca o número nessa gaveta e empurra o resto!
                print(f'Adicionado na {pos} lista')
                break  # Já achamos o lugar dele, então paramos de procurar!
            pos += 1  # Se não for ali, passamos para a próxima gaveta
print('#*'*30)
print(f' os valores digitados em ordem foram {lista}')

'''# Exercício 80 — Entendendo o Encaixe de Valores (Insertion Sort)
## Conceitos Práticos: Varredura Linear e Inserção Indexada Sem Ordenação Tardia

Este exercício simula o comportamento mecânico de organizar elementos em tempo real, eliminando a necessidade de ordenar a estrutura após a coleta de dados.

---

## 1. Os Dois Caminhos do Fluxo

Cada número digitado pelo usuário segue um de dois caminhos lógicos no programa:

### Caminho Rápido (Final da Lista)
Se a lista estiver vazia ou o número for maior que o último elemento atual (`n > lista[-1]`), o Python não perde tempo procurando: ele usa o `.append(n)` para jogar o valor direto no fim.

### Caminho de Busca (Meio ou Início da Lista)
Se o número for menor que o último, o ponteiro `pos` começa no `0` e vai testando item por item. Assim que encontrar um elemento na lista que seja maior ou igual ao número digitado (`n <= lista[pos]`), o algoritmo faz a inserção ali e interrompe a busca com o `break`.

---

## 2. Visualização dos Índices Modificados

Ao usar o `.insert(pos, n)`, o Python automaticamente reorganiza as chaves da memória:

* **Antes:** `[2, 7, 9]` (Índices: 0, 1, 2)
* **Comando:** `lista.insert(1, 5)`
* **Depois:** `[2, 5, 7, 9]` (O 5 assume o índice 1; o 7 e o 9 são empurrados para os índices 2 e 3).'''



