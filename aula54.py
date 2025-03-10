"""
enumerate - enumra iteráveis(indices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = list(enumerate(lista))

print(lista_enumerada)

for tupla_enumerada in enumerate(lista):
   print('FOR da tupla: ')
   for valor in tupla_enumerada:
      print(f'\t{valor}')
