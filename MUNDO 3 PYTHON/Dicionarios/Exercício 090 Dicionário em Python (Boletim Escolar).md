# 👑 Exercício 090: Dicionário em Python (Boletim Escolar)

Este repositório apresenta a resolução oficial do **Exercício 090** do módulo de Dicionários (Módulo 3) do Curso em Vídeo, com uma implementação de lógica de negócios expandida.

## 🚀 Diferencial do Projeto
Diferente do escopo padrão que solicitava apenas a leitura da média pronta, este script foi desenvolvido para capturar as notas individuais (`nota1` e `nota2`), realizando o cálculo aritmético da média diretamente dentro da estrutura do dicionário.

## 🧠 Regras de Negócio Aplicadas
O programa classifica o status acadêmico do aluno com base nas seguintes diretrizes:
- **Média $\ge$ 7.0**: Situação definida como `Aprovado`.
- **Média entre 5.0 e 6.9**: Situação definida como `Recuperação`.
- **Média < 5.0**: Situação definida como `Reprovado`.

## 💻 Resultado no Console

Ao rodar o script `ex.090(dicionario_aluno).py`, o terminal exibe a formatação limpa mapeando chaves (`keys`) e valores (`values`):

```text
Digite o nome do aluno: Ton
Digite a primeira nota: 8.5
Digite a segunda nota: 6.5
----------------------------------------
Dicionário bruto: {'nome': 'Ton', 'nota1': 8.5, 'nota2': 6.5, 'media': 7.5, 'situacao': 'Aprovado'}
----------------------------------------
 - Nome é igual a Ton
 - Nota1 é igual a 8.5
 - Nota2 é igual a 6.5
 - Media é igual a 7.5
 - Situacao é igual a Aprovado