entrada = input("Entrar ou Sair:")
senha = input("Digite a senha: ")

senha_permitida = '12345'
if entrada  == 'E' and senha == senha_permitida:
    print("entrou")
elif entrada  =='S'  =='s':
    print('Saiu')
else:
    print("Comando inválido")