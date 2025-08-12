numero = int(input('Informe um numero: '))

print(f'O hexadecimal de {numero} é {numero:08X}')

exercicio 
nota = 6

while True:
    entrada = int(input('Informe uma note de 0 a 10: '))
    if entrada == nota:
        print(f'Nota {entrada} corrata, acertou miseravel!!')
        break
    
    if entrada != nota:
         print(f'Nota {entrada} incorreta, por favor tente novamente.')
         continue
print('Programa encerrado.')   