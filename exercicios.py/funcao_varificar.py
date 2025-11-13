def verificar_numero(nome, escopo = globals()):# trata o codigo como um dicionario, buscando o nome da variavel dentro do dicionario
    
    if nome in escopo: # verifica se a variavel existe no escopo do codigo
        valor = escopo[nome] # atribui a variavel valor ao nome encontrado no codigo
    else:
        valor = None # se a variavel estiver 'vazia' ele nao veirifca

        while not isinstance(valor, float): # faz a verificação se a variavel já não é do tipo que estamos ultilizando no codigo. se já for desse tipo, o laço while para.
            
            try: # apos a verificação do while ser negativa, tentamos modificar o tipo da  variavel.
                valor = float(input('Digite um numero: ')) # aqui tentamos modificar a variavel para certificar que o valor digitado é um numero real.
                escopo[nome] = valor # aqui a variavel é atribuida ao programa apos a varificação ter dado certo 

            except ValueError:
                    print('Valor invalido. Tente novamente.')# Se o valor informado nao for em um formato que possa ser modificado para float, ele retorna ao usuario pedindo um numero valido.

        return valor                
                    


x = verificar_numero('x')


y = verificar_numero('y')

resultado = x + y
print(resultado)

''' while True:
        try:
            x = input('')
            x_float = float(x)
            break 
        except ValueError:
            print('Informe o primeiro numero novamente: ')
            
    
    while True:
        try:
            y = input('')
            y_float = float(y)
            break 
    
        except ValueError:
            print('Informe o segundo numero novamente: ')'''