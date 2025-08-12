import random 

lista_numeros = []

for _ in range(10):
    lista_numeros.append(random.randint(1,100))
    
print(lista_numeros)

maior = max(lista_numeros)
print(f'O maior numero sorteado foi {maior}')