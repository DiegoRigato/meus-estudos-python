
'''Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.'''


import os
numeros_validos = None

while True:
     
     fatorial = input('Informe um nomero para calacular o fatiral: ')
     resultado = 1
    
     try:
       fatorial_int = int(fatorial)
       numeros_validos = True
     except:
        numeros_validos = None

     if fatorial_int is not None and fatorial_int <= 16:
        for i in range(fatorial_int,0, -1 ):
            resultado *= i
     
     else:
        print('Inform um numero valido. Numero positivo e menor que 16.')   
        continue

     print(resultado)    
    
     continuar = input('Deseja continuar calculando? (s/n)').lower()
     if continuar != 's':
        print('Finalizando programa.')
        break
     os.system('cls')