'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''

primeiro_numero = int(input('Por favor informe o primeiro numero: '))
segundo_numero = int(input('Por fabor informe o segundo numero: '))
lista_intervalo = []
i = 0

for i in range(primeiro_numero, segundo_numero + 1): # somamos mais 1 para aparecer
    lista_intervalo.append(i)                       # o ultimo numero do intervalo.

print(lista_intervalo)