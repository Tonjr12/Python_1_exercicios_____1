# 🎲 Exercício 091: Jogo de Dados em Python (Ordenação de Dicionários)

Este repositório apresenta a resolução do **Exercício 091** do módulo de Dicionários (Módulo 3) do Curso em Vídeo. O foco deste desafio é a manipulação avançada e ordenação de estruturas de dados compostas.

## 🚀 Objetivo do Projeto
O programa simula 4 jogadores virtuais que lançam um dado de 6 faces simultaneamente. Os resultados aleatórios são armazenados em um dicionário e, posteriormente, tratados para gerar um ranking do vencedor ao quarto colocado.

## 🧠 Conceitos Avançados Praticados
- **Geração Aleatória (`random.randint`)**: Utilizado para simular o comportamento físico dos dados.
- **Efeito de Delay (`time.sleep`)**: Implementação de temporizador no console para simular a expectativa do sorteio.
- **Ordenação Dinâmica (`operator.itemgetter`)**: Uso da função integrada `sorted()` combinada com `itemgetter(1)` para contornar a limitação nativa de ordenação de dicionários, organizando a estrutura com base nos valores (`values`) e convertendo os dados em uma lista ordenada de tuplas.

## 💻 Saída Esperada no Console

```text
🎲 VALORES SORTEADOS: 🎲
O jogador1 tirou 6 no dado.
O jogador2 tirou 2 no dado.
O jogador3 tirou 5 no dado.
O jogador4 tirou 1 no dado.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
🏆 RANKING DOS JOGADORES 🏆
   1º lugar: jogador1 com 6.
   2º lugar: jogador3 com 5.
   3º lugar: jogador2 com 2.
   4º lugar: jogador4 com 1.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=