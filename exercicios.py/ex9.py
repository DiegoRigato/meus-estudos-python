'''Altere o ex8 anterior para mostrar no final a soma dos números.'''


primeiro_numero = int(input('Por favor informe o primeiro numero: '))
segundo_numero = int(input('Por favor informe o segundo numero: '))
lista_intervalo = []
i = 0

for i in range(primeiro_numero, segundo_numero + 1): # somamos mais 1 para aparecer
    lista_intervalo.append(i)                       # o ultimo numero do intervalo.

print(lista_intervalo)

for i in lista_intervalo:
    soma += i
print(soma)