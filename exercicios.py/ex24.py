import os
lista_idade = []

while True:

    while True:
        tamanho = input('Informe quantas pessoas tem no seu grupo:  ')

        try:
            tamanho_int = int(tamanho)
            break

        except ValueError:
            print('Informe um numero inteiro.')

    for i in range(tamanho_int):
        while True:

            idade = input(f'Informe a {i + 1}ª idade: ')

            try: 
                idade_int = int(idade)
                lista_idade.append(idade_int)
                break 

            except ValueError:
                print('Informe um numero inteiro.')       

    soma = 0

    for j in (lista_idade):
        soma += j 

    media = soma / tamanho_int

    if media <= 25:
        print('Turma de jovens.')      

    elif media >= 26 and media <= 60:
        print('Turma de adultos.')      

    else:
        print('Turma da melhor idade.')


    continuar = input('Deseja fazer outra operação? (s/n)').strip().lower()
    if continuar != 's':
        print('Programa encerrado.')
        break
    else:
        lista_idade.clear()

    os.system('cls')    