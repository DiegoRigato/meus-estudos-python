'''Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.'''

numero = int(input('Informe um numero: '))
eh_primo = True


if numero <= 1:
    eh_primo = False

else:
    for i in range (2, numero):# o for vai testar ate o n - 1. 
        if numero % i == 0:
            eh_primo = False
            break
             
if eh_primo:
    print(f'O numero {numero} é um numero primo.')

else:
    print(f'O numero {numero} não é um numero primo.')



