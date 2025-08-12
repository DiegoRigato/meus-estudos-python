'''Iteravel -> str, range, etc
Iterador -> quem sabe entregar um valorpor vez
nexr -> me entrega o proximo valor
iter -> me entregue seu interador'''


# numeros = range(0, 100, 8)

# for numero in numeros:
#     print(numero)


texto = 'Diego' # iteravel

iterador = iter(texto) # iterador


while True:
    try:
        letra = next(iterador)
        print(letra)

    except StopIteration:
        break    

'''O codigo acima é o mesmo que:

for letra in texto:
    print(letra)
    '''