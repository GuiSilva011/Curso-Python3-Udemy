"""
Exercício
PEÇA AO USUÁRIO PARA DIGITAR SEU NOME
PEÇA AO USUÁRIO PARA DIGITAR SUA IDADE
Se o nome e idade forem digitados:
    Exiba:
        seu nome é {nome}
        seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios"

"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if '' not in nome or idade:
    print(f'Seu nome é {nome}')

    print(f'seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")

    print(f'Seu nome contém {len(nome)} letras')

    print(f'A primeira letra do seu nome é {nome[0::-1]}')

    print(f'A última letra do seu nome é {nome[-1::]}')
else:
    print('Voce deixou campos vazios')



