'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

lista_numeros = []
i = 0
soma = 0

while i < 5:
    numero = int(input(f'Por favor insira o {i + 1}ª numero: '))
    lista_numeros.append(numero)
    i += 1

for numero in lista_numeros:
    soma += numero  
media = soma / 5    
print(f'Os numeros inseridos na litsa foram: {lista_numeros}')    
print(f'A soma de todos os numeros é: {soma}')  
print(f'A media dos numeros inseridos é: {media:.0f}')