"""
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de 
inserir,apagar e listar valores da sua lista
Não permita que o pgrama quebre com 
erros de índices inexistentes na lista.
"""


print('Selecione uma opção')

carrinho = []

while len(carrinho) < 100:
        opc = input('[I]nserir,[A]pagar,[L]istar: ')
        if opc == 'I':
            valor = input('Valor: ')
            carrinho.append(valor)
           
        if opc =='L' and len(carrinho) <= 0:
            print('Carrinho vazio...')
        elif opc == 'L' and len(carrinho) >= 1:
            indices = range(len(carrinho))
            for indice in indices:
                print(indice,carrinho[indice])
                
        if opc == 'A':
            delete = int(input('indique o indice a ser removido da lista: '))
            for indice in indices:
                 print(indice,carrinho[indice])
            if delete == indice:
                 carrinho.pop(delete)
                 print('Indice apagado com sucesso.')
                

 
        

     