# Faça um programa que calcule o mostre a média aritmética de N notas.

import os

lista_notas = []


while True:

    while True:
        tamanho = input('Infome quantas notas vai querer inserir: ')
    
        try: 
            tamanho_int = int(tamanho)
            break

        except:
            print('Por favor infome um numero inteiro.')   

       
    for i in range(tamanho_int):
        while True:
            notas_alunos = input(f'Infome a {i + 1}ª nota: ')

            try:
                notas = float(notas_alunos)
                lista_notas.append(notas)
                break
            
            except ValueError:
                print('Informe um numero.')

    print(f'\nAqui esta a lista com as notas: {lista_notas}')
    
    soma = 0
    for j in (lista_notas):
        soma += j

    print(f'\nAqui esta a soma de todas as notas: {soma}')    

    media = soma / tamanho_int
    print(f'\nAqui esta a media das notas: {media:.1f}') 

    continuar = input('\nDeseja fazer outra operação? (s/n)').strip().lower()
    if continuar != 's':
        print('Programa finalizado.')
        break

    else:
        lista_notas.clear()

    os.system('cls')
