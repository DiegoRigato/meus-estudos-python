while True: 
    nome = input('Informe seunome: ')
    tamanho_nome = len(nome)
    
    if tamanho_nome < 3:
        print("Nome muito curto. Digite novamente.")
    else:
        break
   
while True:
        
    idade = int(input('Informe sua idade: '))
    if idade < 0 or idade > 150:
            print("Idade incorreta. Por favor repita.")
    else:
        break
    
while True :   
    salario = float(input("Informe seu salario: "))
    if salario <= 0:
            print('Salario informado incorreto. Por favor tente novamente.')
    else:
        break
    
while True:        
    estado_civil = input('Informe seu estado civil (s, c, v, d): ')
    if estado_civil == "s":
        break
    elif estado_civil == 'c':
        break
    elif estado_civil == 'v':
        break
    elif estado_civil =='d':
        break
    else:
        print('Estado civil incorreto. Tente novamente.')
    
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salario: {salario}')
print(f'Estado civil: {estado_civil}')
