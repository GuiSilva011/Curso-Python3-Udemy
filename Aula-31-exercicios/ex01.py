"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    n1 = int(input('Digite um numero inteiro: '))
    if n1 % 2 == 0:
     print('é par')
    else:
        print(f'{n1.isdigit()}')
except:
   print('Não é um numero inteiro')
