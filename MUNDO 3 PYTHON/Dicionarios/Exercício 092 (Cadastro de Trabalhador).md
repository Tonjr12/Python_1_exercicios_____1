# 💼 Exercício 092: Cadastro de Trabalhador

Resolução do desafio de dicionários do Curso em Vídeo, com implementação de **lógica de cálculo própria**.

## 🚀 Diferencial do Projeto
Neste exercício, a lógica de cálculo para a aposentadoria foi otimizada para uma leitura mais intuitiva:
1. Cálculo da idade de início de carreira: `Ano Contratação - Ano Nascimento`.
2. Projeção da aposentadoria: `Idade Início + 35 anos de contribuição`.

## 🧠 Conceitos Aplicados
- **Dicionário Dinâmico**: O dicionário cresce conforme a condição do usuário (possuir ou não CTPS).
- **Manipulação de Datas**: Uso do `datetime.now().year` para manter o sistema sempre atualizado.
- **Estrutura Condicional**: Uso de `if/else` para validar dados de entrada.

## 💻 Exemplo de Execução
```text
Nome: Ton
Ano de nascimento: 1990
Carteira de trabalho (0: nao tem): 1234
------------------------------
Ano de contratação: 2015
Salario: 3000
------------------------------
 - Nome tem o valor Ton
 - Idade tem o valor 36
 - Ctps tem o valor 1234
 - Contratação tem o valor 2015
 - Salario tem o valor de R$ 3000.00
 - Idade_aposentadoria tem o valor 60