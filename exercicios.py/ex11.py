'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.'''


encerrar = False
while not encerrar:
    iniciar = input('Gostaria de iniciar a calculadora de potencia? (s/n)')
    
    if iniciar.lower() == 's':
        numero_1 = int(input('\nInforme o valor da base: '))
        numero_2 = int(input('\nInfome o valor de expoente: '))
        resultado = numero_1 ** numero_2
        print(f'\nO resultado de {numero_1} elevado ao {numero_2} é {resultado}')
        
        repetir = input('Deseja fazer um novo calculo? (s/n)')
        if repetir.lower() != 's':
            encerrar = True
            break
    
    elif iniciar.lower() == 'n':
        print('Programa finalizado.')
        break
    
    else:
        print('Escolha uma opção valida.')