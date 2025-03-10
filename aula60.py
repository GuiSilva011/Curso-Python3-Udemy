#desempacotamento em chamadas
#de metodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1,2,3,'Eduarda']
tupla = 'python', 'é' , 'legal' 


p,b, *_,u= lista
print(p,u)

print('Maria','Helena',1,2,3,'Eduarda')
print(*lista)
print(*string)
print(*tupla)