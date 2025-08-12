while True:
    nome = input('Informe o nome do usuario: ')
    senha = input('Informe uma senha')
    if senha != nome: 
        print(f'Nome de usuario e senha cadastrado com sucesso.')
        break
    else:
        print(f'Nome de usuario e senha iguais, por favor tente novamente.')
        continue
print('Programa encerrado.')
