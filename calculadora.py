# Desenvolva um calculadora que receba dois números e efetue uma das seguintes operações aritméticas:

#    1 - Adição
#    2 - Subtração
#    3 - Multiplicação
#    4 - Divisão
#    5 - Potência
#    6 - Raiz quadrada
#    7 - Número par
#    8 - Número ímpar

#=============================================================================================================

import math

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação desejada: ')

if operacao == '+':
    print(f'O resultado da somoa é {num1 + num2:.2f}')
elif operacao == '-':
    print(f'O resultado da subtração é {num1 - num2:.2f}')
elif operacao == '*':
    print(f'O resultado da multiplicação é {num1 * num2:.2f}')
elif operacao == '/':
    print(f'O resultado da divisão é {num1 / num2:.2f}')
elif operacao == '^':
    pot = float(input('Qual potencia quer elevar ? '))
    print(f'O resultado da potencia do primeiro número é {pow(num1, pot):.2f}')
    print(f'O resultado da potencia do segundo número é {pow(num2, pot):.2f}')
elif operacao == 'raiz':
    print(f'A raiz quadrada do primeiro número é {math.sqrt(num1):.2f}')
    print(f'A raiz quadrada do segundo número é {math.sqrt(num2):.2f}')
elif operacao == 'par/impar':
    if num1 % 2 == 0:
        print('O primeiro número é par')
    else:
        print('O primeiro número é impar')
    if num2 % 2 == 0:
        print('O segundo número é par')
    else:
        print('O segundo número é impar')
else:
    print('Opção invalida')