'''Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.'''


lista_impar = []

lista_numeros = list(range(1,51))# jeito simples de gerar uma lista ordenada.    
print(lista_numeros)  

for numero in lista_numeros:
    if numero % 2 != 0:
        lista_impar.append(numero) # aqui criei outra lista para if add nela   
                                   # os numero impares para serem impressos
                                   
print(f'\nOs numeros impares da lista são: {lista_impar}')