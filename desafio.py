# Primera pergunta:
# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será
# a soma dos 2 valores anteriores, escreva um programa onde, informado um número,
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número
# informado pertence ou não à sequência.

# Solução:

number = int(input("Informe um número: "))

fib_sequence = [0, 1]

while fib_sequence[-1] < number:
    next_fib = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_fib)

if number in fib_sequence:
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")

# Segunda pergunta:
# Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
# seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
# Essa string pode ser informada através de qualquer entrada de sua preferência 
# ou pode ser previamente definida no código.

string = input("Informe uma string: ")

amount_a = string.lower().count('a')

if amount_a > 0:
    print(f"A letra 'a' aparece {amount_a} vez na string.")
elif amount_a > 1:
    print(f"A letra 'a' aparece {amount_a} vezes na string")
else:
    print("A letra 'a' não está presente na string.")

# Teceira pergunta:
# Observe o trecho de código abaixo:
# int INDICE = 12,
# SOMA = 0, K = 1;
# enquanto K < INDICE faça {
#   K = K + 1;
#   SOMA = SOMA + K;
# }
#
# imprimir(SOMA);
#
# Ao final do processamento, qual será o valor da variável SOMA?

INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K += 1
    SOMA += K

print(SOMA)  # Isso imprimirá 77

# Quarta pergunta:

# 4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, ___ (9)
# b) 2, 4, 8, 16, 32, 64, ____ (128)
# c) 0, 1, 4, 9, 16, 25, 36, ____ (40)
# d) 4, 16, 36, 64, ____ (100)
# e) 1, 1, 2, 3, 5, 8, ____ (13)
# f) 2,10, 12, 16, 17, 18, 19, ____ (20)

# Quinta pergunta:

# Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes.
# Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser.
# Seu objetivo é descobrir qual interruptor controla qual lâmpada.
# Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas,
# qual interruptor controla cada lâmpada?

# Para descobrir qual interruptor controla cada lâmpada, iremos seguir os passos abaixo:

# 1. Ligar o primeiro interruptor e deixe-o ligado por cerca de 10 minutos.
# 2. Desligar o primeiro interruptor e ligar o segundo interruptor.
# 3. Deixe o terceiro interruptor desligado durante todo o processo.
# 4 Ir até a sala das lâmpadas e verifique o estado das lâmpadas:
# - Lâmpada acesa: Esta lâmpada é controlada pelo segundo interruptor, que está ligado.
# - Lâmpada apagada, mas quente: Esta lâmpada é controlada pelo primeiro interruptor,
#   que estava ligado por 10 minutos e depois foi desligado.
# - Lâmpada apagada e fria: Esta lâmpada é controlada pelo terceiro interruptor,
#   que permaneceu desligado o tempo todo.

# Dessa forma, podemos  identificar qual interruptor controla cada lâmpada.
