"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = "Guilherme"
preco = 1000.493943
variavel = '%s, o preço total é R$%f' % (nome,preco)
print(variavel)

print('O hexadecimal de %d é %4x' % (1500,1500))