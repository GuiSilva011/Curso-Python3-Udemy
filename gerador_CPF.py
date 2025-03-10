import random



nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))




contador_regressivo_1 = 10

resultado_1 = 0

for digito_1 in nove_digitos:
    
    resultado_1 += (int(digito_1) * contador_regressivo_1)
    contador_regressivo_1 -=1
digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado_2 = 0

for digito_2 in dez_digitos:

    resultado_2 += (int(digito_2) * contador_regressivo_2)
    contador_regressivo_2 -=1
digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_gerado == cpf:
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')