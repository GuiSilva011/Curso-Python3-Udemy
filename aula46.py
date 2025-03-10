"""
Faça um jogo para o usuário adivinhar qual a
palavra secreta.
Voce vai propor uma palavra secreta qualquer e vai dar a possbilidade
para o usuário digitar apenas uma letra.
Quando o usuario digitar uma letra, voce vai conferir se a letra
digitada esta na palavra secreta.
    -Se a letra digitada estiver na palavra secreta;
    exiba a letra;
    -Se a letra digitada não estiver na palavra secreta;Exia *.
    -Faça a contagem de tentativa do seu usuário
"""
import os

palavra_secreta = 'garibaldo'
letras_acertadas = ''
num_tentativas = 0
while True:
 
    letra = input('Digite uma letra: ')
    num_tentativas += 1
    if len(letra) > 1:
        print('Digite apenas uma letra. ')
        continue
    
    if letra in palavra_secreta:
        letras_acertadas += letra
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
           palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada: ', palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!!')
        print('A palavra era:',palavra_secreta)
        print('Tentativas:', num_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
       
        
