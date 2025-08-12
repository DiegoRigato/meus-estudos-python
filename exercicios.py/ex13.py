'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.'''


while True:
    numeros = []
    numeros_pares = []
    numeros_impares = []
    
    for i in range(10):
        while True:
            entrada = input(f'Informe o {i + 1}º numero inteiro: ')
            try:
                numero = int(entrada)
                numeros.append(numero) 
                break
            except:
                print('Informe apenas numeros inteiros.')
   
    print(f'\nNumero digitado {numeros}')
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
            

    for numero in numeros:
        if numero % 2 != 0:
            numeros_impares.append(numero) 

    qtd_numeros_pares = len(numeros_pares)       
    qtd_numeros_impares = len(numeros_impares)

    print(f'\nVocê informou uma quantidade de {qtd_numeros_pares} numeros pares, esses foram os numeros {numeros_pares}')
    print(f'\nVocê informou uma quantidade de {qtd_numeros_impares} numeros impares, esses foram os numeros {numeros_impares}')           

    sair = input('\nDeseja sair? [s]im').lower().startswith('s')
    print('Programa finalizado.')
    if sair is True:
        break