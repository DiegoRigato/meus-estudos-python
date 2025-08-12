"""
Lista em Python
Tipo list - Multável
Suporta varios valores de qualquer tipo 
Conheciomentos reutilizaveis - indice e fatiamento
Metodos uteis: append, insert, pop, del, clear, extend, +

Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

string = 'ABCDE' # 5 caracteres (len)
lista = [123, True, 'Luiz Otávio', 1.2, []]
lista[-3] = 'Maria'# aqui podemos alterar o valor do indice da lista (pode ser - 3 ou 2).
print(lista)
print(lista[2].upper(), type(lista[2]))# aqui podemos aplicar funções dentro da lista, e verificar o tipo de cada variavel

#print(bool(lista)) = falsy
#print(lista, type(lista))