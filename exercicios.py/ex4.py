'''Supondo que a população de um país A seja da ordem de 80_000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200_000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''

import math # importa a biblioteca de matematica

taxa_populacao_maior = 1.03
taxa_populacao_menor = 1.015
razao_pop = 200000/80000

t = math.log(2.5) / math.log(1.03/1.015) # usa a função logaritimica da bibliota math

t_anos =math.ceil(t) # Função ceil arredonda para cima os valores

encerrar = False

while not encerrar: 
    iniciar = input('\nDeseja iniciar o programa? (s/n)')

    if iniciar.lower() == 's':

            while True:
                populacao_maior = int(input('\nInforme o tamanho da pupulação maior: '))
                populacao_menor = int(input('\nInfoprme o tamanho da população menor: '))
                taxa_populacao_maior = float(input('\nInforme a taxa de crescimento da população maior (%): '))
                taxa_populacao_menor = float(input('\nInforme a taxa de crescimento da população maior (%): '))

                anos = 0
                t_populacao_maior = (taxa_populacao_maior / 100) + 1
                t_populacao_menor = (taxa_populacao_menor / 100) + 1

                while populacao_menor < populacao_maior:
                    populacao_maior *= t_populacao_maior
                    populacao_menor *= t_populacao_menor
                    anos += 1

                print(f'\nLevara {anos} anos para a população A ultrapassar ou igualar a de B.')
                print(f'O pais a tera {populacao_maior:.0f} habitantes.')
                print(f'O pais a tera {populacao_menor:.0f} habitantes.')
                repetir = input('\nDeseja fazer outro calculo? (s/n)')

                if repetir.lower() != 's':
                    print('Encerrando programa....')
                    encerrar = True # para encerra todo o programa poderia criar uma nova
                    break           # ou importar a função sys. criando a nova variavel
                                    # o programa entende que é para encerrar tudo.

    elif iniciar.lower() == 'n':
        print('Programa finalizado.')
        break

    else:
        print('Escolha uma opção valida.') 