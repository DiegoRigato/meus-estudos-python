'''Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.'''


numero = int(input('Informe um numero: '))
eh_primo = True
x = 1
numeros_divisores = [x, numero]


if numero <= 1:
    eh_primo = False

else:
    for i in range (2, numero):# o for vai testar ate o n - 1. 
        while numero % i == 0:
            numeros_divisores.append(i)# incluimos i a lista
            eh_primo = False
            break

divisores_ordenados = sorted(numeros_divisores)# ordenamos a lista de numeros divisores.

if eh_primo:
    print(f'O numero {numero} é um numero primo.')
    print(f'Os numero que dividem ele: {numeros_divisores}')

else:
    print(f'O numero {numero} não é um numero primo.')
    print(f'Os numero que dividem ele: {divisores_ordenados}')



