qtd_linas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=},{coluna=}')
        coluna +=1
    linha +=1

print('ACABOU')