'''Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.'''



# numero = int(input('Informe um numero: '))
# lista_do_usuario = []
# # divisoes = 0 
# x = 0


# for n in range(1, numero + 1):   # vai até o número digitado (inclusive)
#     if n <= 1:
#         continue                 # 0 e 1 não são primos

#     eh_primo = True

#     for i in range (2, numero):
#         if numero % i == 0:
#             x = numero
#         lista_do_usuario.append(x) 
#         break
    
#     for d in range(2, n + 1):    # inclui n (por isso tratamos d == n)
#         if d == n:
#             # chegamos ao próprio n e não achamos divisor antes -> é primo
#             break
#         if n % d == 0:
#             eh_primo = False
#             break

#     if eh_primo:
#         lista_do_usuario.append(n)

# print(lista_do_usuario)

numero = int(input('Informe um número: '))
lista_do_usuario = []

for n in range(1, numero + 1):   # testa todos até o número informado
    if n <= 1:
        continue                 # pula 0 e 1, que não são primos

    eh_primo = True

    for d in range(2, n):
        if n % d == 0:
            eh_primo = False
            break

    if eh_primo:
        lista_do_usuario.append(n)

# Agora, adiciona `numero` à lista se ele **não for primo**:
# Só adiciona uma vez.
if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            lista_do_usuario.append(numero)
            break

print(lista_do_usuario)