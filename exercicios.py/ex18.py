'''Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.'''



lista_numero = []
tamanho = int(input('Informe quantos numeros quer calcular: '))
soma = 0
numero_int = 0
numeros_validos = None

while len(lista_numero) != tamanho:
    numero = input(f'Informe um numero: ')
    try:
       numero_int = int(numero)
       numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Por favor digite um numero inteiro.')
        continue

    if numero_int >= 0 and numero_int <= 1000: # aqui nao esta sendo executado
        lista_numero.append(numero_int)
       
    else:
        print('Informe um numero entre 0 e 1000.')
        continue
    
    
for numero in lista_numero:
    soma += numero

print(f'Aqui esta os numero que você informou: {lista_numero}')     

print(f'A soma de todos os numero é: {soma}')

maior = max(lista_numero)
print(f'O maior numero da lista é: {maior}')

menor = min(lista_numero)
print(f'O menor numero da lista é: {menor}')
