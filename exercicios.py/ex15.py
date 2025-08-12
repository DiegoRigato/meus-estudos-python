'''A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.'''


'''Para gerar a sequencia ate ela atingir o valor 500, precisamos fazer algumas alterações no codigo. agora nomeamos duas variaveis para iniciar a sequencia e apartir dela gerar os calculos.'''




a = 1 # 'a' e 'b' inicam a sequencia.
b = 1
lista = [ a, b] # adicionamos elas a lista onde geraremos o restante da sequencia.
  

while True:
    proximo = a + b
    if proximo >= 987: # criamos a variavel de controle 'proximo', que serar responsavel de para o laço em 500.
        break
    lista.append(proximo)
    a = b
    b = proximo
print(lista)           
   
           
           
   
   