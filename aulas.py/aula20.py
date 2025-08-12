numero_1 = input('Informe um numero: ')
numero_2 = input('Informe outro numero: ')

if numero_1 > numero_2:
    print(f'O primeiro numero {numero_1}, é maior que o segundo numero.')

elif numero_2 > numero_1:
    print(f'O segundo numero {numero_2}, é maior que o primeiro numero.')    

elif numero_1 == numero_2:
    print(f'Os numero são iguais.')

else:
    print('Digite um numero.')    