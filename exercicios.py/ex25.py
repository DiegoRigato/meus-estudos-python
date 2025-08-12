# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

import os



while True:

    acm_neto = 0
    pelegrino = 0
    uilton = 0
   
    while True:
        eleitores = input('Informe o numero de votantes: ')
    
        try: 
            eleitores_int = int(eleitores)
            break
        except:
            print('Informe um numero.')

    print('Numero nos candidatos:')
    print('ACM Neto - 25')
    print('Pelegrino - 13')
    print('Uilton - 50')


    for i in range(eleitores_int):

        while True:
            
            voto = input('Informe o numero do seu candidato: ')
            try:
                voto_int = int(voto) 
                break
            except:
                print('Informe um numero valido.')

        if voto_int == 25:
            
            while True:
                confirmacao = input(f'Você votou em ACM Neto, certo? (s/n)').strip().lower()
                if confirmacao == 's':    
                    acm_neto += 1
                    break
                elif confirmacao == 'n':
                   print('Vamos tentar novamente...')
                   break
                else:
                    print('Digite apenas "s" ou "n".')

        elif voto_int == 13:
            while True:
                confirmacao = input(f'Você votou em Pelegrino, certo? (s/n)').strip().lower()
                if confirmacao == 's':
                    pelegrino += 1
                    break
                elif confirmacao == 'n':
                    print('Vamos tentar novamente...')
                    break
                else:
                    print('Digite apenas "s" ou "n".')    

        elif voto_int == 50:
            while True:
                confirmacao = input(f'Você votou em Uilton, certo? (s/n)').strip().lower()
                if confirmacao == 's':
                    uilton += 1
                    break
                elif confirmacao == 'n':
                    print('Vamos tentar novamente...')
                    break
                else:
                    print('Digite apenas "s" ou "n".') 

        else:
            print('Por favor informe um numero de candidato valido.')            

    print(f'O cadidato ACM Neto teve {acm_neto} votos.')
    print(f'O cadidato  Pelegirno teve {pelegrino} votos.')
    print(f'O candidato Uilton teve {uilton} votos.')

    novamente = input('Deseja fazer uma nova votação? (s/n) ').strip().lower()
    if novamente != "s":
        print('Programa finalizado.')
        break 
    else:
        os.system('cls')
        continue                                

