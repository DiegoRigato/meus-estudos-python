"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Informe um numero inteiro: ')

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
     print(f'O numero {numero_int} é par.')

    elif numero_int % 2 != 0:
       print(f'O numero {numero_int} é impar.') 

except:
   print('Você não digitou um numero inteiro.')       