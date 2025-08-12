frase = 'O Python é uma linguagem de programação multiparadigma Python foi criado por guido van Rossum'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ': # imepede que o programa conte os espaçoes
        i += 1 # incrementa o i ja retirando os espaços.
        continue

    qtd_vezes_letra_apareceu_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_vezes_letra_apareceu_atual:
        qtd_apareceu_mais_vezes = qtd_vezes_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual

    
    i += 1
print(f'A letra que mais apareceu foi "{letra_apareceu_mais_vezes}", Ela apareceu {qtd_apareceu_mais_vezes}X')    