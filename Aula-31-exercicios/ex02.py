"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    horario = float(input('Que horas são?: '))
    if horario >= 0 and horario <= 11:
        print('Bom dia')
    elif horario < 17:
        print('Boa tarde')
    elif horario <= 23:
        print('Boa noite')
except:
    print('Você digitou algo inválido')

  
