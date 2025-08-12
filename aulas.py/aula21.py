# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor


# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:  
    #print('Entrar')                                          
# else:                                                        
     #print('Sair')                                        
                                                              

"""Se usar o elif apos esse if, teria que informa a
condição do S, pois se o usuario nao digitasse o s o 
sistema nao iria reconhecer. Desta forma que foi feito ele entende qualquer coisa que nao seja o S. """



# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)