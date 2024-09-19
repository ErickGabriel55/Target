"""1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

# Inicia a lista do fibonacci e pergunta ao usuário
fibonacci = [0, 1]
numero = int(input("Qual número deseja verificar se está na sequência de fibonacci? "))

while True:
    # verifica se o numero fornecido pelo usuario é menor que o ultimo da lista
    if numero < fibonacci[-1]:
        # se for, a mensagem é exibida e programa é interrompido
        print(f"O número {numero} não encontrado na sequência fibonacci!\nlista atual {fibonacci}")
        break
    # verifica se o número foi encontrado
    elif numero == fibonacci[-1]:
        indice = fibonacci.index(numero)
        print(f"O número {numero} foi encontrado na posição {indice + 1}!\nlista atual {fibonacci}")
        break
    # verfica se o numero é maior
    elif numero > fibonacci[-1]:
        # caso seja continua a incrementação da lista
        somaFibonacci = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(somaFibonacci)
