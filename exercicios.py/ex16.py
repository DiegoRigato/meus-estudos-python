'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120'''

'''
Fatorial de forma simples com while:

fatorial = int(input('Informe o numero para calcular o fatorial: '))
resultado = 1

while fatorial != 0:
    resultado *= fatorial
    fatorial -= 1

print(resultado)     
'''

fatorial = int(input('Informe um nomero para calacular o fatiral: '))
resultado = 1

for i in range(fatorial,0, -1 ):
    resultado *= i


print(resultado)    
