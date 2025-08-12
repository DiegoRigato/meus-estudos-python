'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.'''

while True:
    lista = [1, 1]
    tamanho = int(input('Informe o tamanho da sequencia: '))

    for i in range(2, tamanho):
        proximo = lista[i - 1] + lista[i -2]
        lista.append(proximo)

    print(lista)    

    encerrar = input('Você gostaria executar novamente? [s]im ').lower().startswith('s')
    if encerrar is False:
        print('Encerrando o programa')
        break