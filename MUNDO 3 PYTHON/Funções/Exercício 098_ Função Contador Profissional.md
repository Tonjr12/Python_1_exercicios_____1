# ⚙️ Exercício 098: Função Contador Profissional

Implementação de uma função de contagem dinâmica com tratamento de dados e lógica modularizada.

## 🚀 O Diferencial desta Resolução
- **Tratamento de Dados (Robustez)**: Implementação de camada de segurança para tratar valores de "passo" inválidos (zero ou negativos), utilizando `abs()` e condições de sanitização para evitar erros em tempo de execução.
- **Lógica Flexível**: A função foi projetada para detectar automaticamente a direção da contagem (progressiva ou regressiva) com base nos parâmetros de entrada, eliminando a dependência de estruturas fixas de `range`.
- **Experiência do Usuário (UX)**: Inclusão de temporizador (`sleep`) para uma visualização otimizada no terminal.

## 🧠 Conceitos Aplicados
- **Modularização**: Encapsulamento da lógica em funções independentes (parâmetros `i, f, p`).
- **Sanitização de Dados**: Higienização dos inputs antes do processamento.
- **Laços de Repetição (`while`)**: Controle de fluxo dinâmico de contagem.