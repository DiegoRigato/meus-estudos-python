'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.'''

lista_numero = []
tamanho = int(input('Informe quantos numeros quer calcular: '))
soma = 0

while len(lista_numero) != tamanho:
    numero = int(input('Informe um numero: '))
    lista_numero.append(numero)

for numero in lista_numero:
    soma += numero

print(f'A soma de todos os numero é: {soma}')

maior = max(lista_numero)
print(f'O maior numero da lista é: {maior}')

menor = min(lista_numero)
print(f'O menor numero da lista é: {menor}')
