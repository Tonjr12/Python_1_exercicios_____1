# Inicia a variável com um valor que NÃO seja o de parada (999)
n = 0
cont = 0
soma = 0

# O 'vigia' só deixa entrar se NÃO for 999
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999: # Só conta e soma se não for o sinal de parada
        soma += n
        cont += 1

print(f'soma {soma} quantidade de numeros digitados {cont}')# Resumo: Flags e Sentinelas (Ponto de Parada)






'''Um software precisa saber exatamente quando parar para não entrar em loop infinito.

### Conceitos Chave:

* **Flag/Sentinela**: É um valor especial (como o 999) que não faz parte 
  dos dados, mas serve apenas para encerrar o processo.
* **Selective Processing**: O uso de um `if` dentro do `while` garante 
  que a flag de parada não seja processada como um dado real (não seja somada)[cite: 14].
* **Input Synchronization**: Ler o dado dentro do laço permite que o 
  "vigia" (`while`) cheque a condição imediatamente na próxima volta[cite: 14].'''