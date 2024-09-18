"""1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

fibonacci = [0, 1]
numero = int(input("Qual número deseja verificar se está na sequência de fibonacci? "))
while True:
    if numero < fibonacci[-1]:
        print(f"O número {numero} não encontrado na sequência fibonacci!\nlista atual {fibonacci}")
        break
    elif numero == fibonacci[-1]:
        indice = fibonacci.index(numero)
        print(f"O número {numero} foi encontrado na posição {indice + 1}!\nlista atual {fibonacci}")
        break
    elif numero > fibonacci[-1]:
        somaFibonacci = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(somaFibonacci)
    