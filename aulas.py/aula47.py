"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'elevador'
letras_acertadas = ''
numero_tentaivas = 0

while True: 
    
    letra_digitada = input('Digite uma letra: ') # Pede ao usuario uma letra.
    numero_tentaivas += 1 # quando digita a letra, conta uma tentativa.
    
    if len(letra_digitada) > 1: #verificamos se foi digitado 1 letra só.
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta: # se a letra estiver na palavra, adicionamos ela.
        letras_acertadas += letra_digitada

    palavra_formada = ''# criamos essa variavel aqui, para ela ser formada fora do for.

    for letra_secreta in palavra_secreta: # verificamos as letras secretas da palavra secreta.
        if letra_secreta in letras_acertadas: # verificamos se tem elas nas letras digitadas.
            palavra_formada += letra_secreta  # adicionamos elas numa nova variavel

        else:
            palavra_formada += '*' # aqui mantem todas as letras que nao foram acertadas com *.

    print(f'Palavra formada = {palavra_formada}') # assim a palavra aparece de forma correta e nao letra sobre letra.            

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Você ganhou.')
        print(f'A palavra era : {palavra_secreta}')
        print(f'Numero de tentativas: {numero_tentaivas}')
        letras_acertadas = ''
        numero_tentaivas = 0
    
        continuar = input('Deseja continuar: (s/n)').lower 
        if continuar == 'n':
            break

        else:
            continue

