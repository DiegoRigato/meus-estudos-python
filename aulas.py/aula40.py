"""calculadora while"""

while True:  

    numero_1 = input('\nDigite um numero: ')
    numero_2 = input('\nDigite outro numero: ')
    operador = input('\nDigite o operador (+ - / *): ')
    
    numeros_validos = None #criada uma flag para verificar os numeros validos.
    num_1_float = 0 # essas 3 são
    num_2_float = 0

    try:
        num_1_float = float(numero_1)# converte os numeros em float
        num_2_float = float(numero_2)
        numeros_validos = True # se a converção de certo ele valida a variavel como True.

    except:
        numeros_validos = None # se a converção de errado ela eh marcada como None ( vazia) e o programa retorna.
                                # o except capitura o erro e muda a variavel para none.

    if numeros_validos is None: # se os numero nao forem validos ele informa ao usuario.
        print('\nUm ou ambos os numeros digitados são invalidos.')  
        continue # com esse continue o programa volta para o inicio   

    operadores_permitidos = '+-/*' # aqui verificamos os operadores permitidos.
    if operador not in operadores_permitidos:# se forem invalidos ele mostra ao usuario
        print('\nOperadore  invalido.')
        continue

    if len(operador) > 1:
        print('\nDigite apenas um operador.')
        continue

    print('\nRealizando sua conta. Confira o resultado abaixo: ')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ',num_1_float + num_2_float)

    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ',num_1_float - num_2_float)


    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = ',num_1_float / num_2_float)        

    elif operador == '*':
        print(f'{num_1_float} x {num_2_float} = ',num_1_float * num_2_float)

    else:
        print('Isso nunca deveria chegar aqui.')    

    sair = input('\nQuer sair? [s]im:').lower().startswith('s')# essas funções: ".lower()" - tranforma a string em
    print('Programa finalizado')                             # minuscula. ".startwith()" verifica se a 
                                                            # string começa com um determinado caracter.
    if sair is True:
        break
                                                        