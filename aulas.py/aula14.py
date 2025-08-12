a = 'A'
b = "B"
c = 1.1
 
string = 'a={nome1} b={nome2} c={nome3:.2f} '# Ultilizando os indices, podemos repetir os numeros e ate mesmo modificar a ordem -> a={0}, b{1}, c={2} ou a={2},b={1},c={0}
formato = string.format(nome1=a,nome2=b,nome3=c)

print(formato)

# Quando dou nome ao argumeto ele se torna um parametro nomeado ex -> nome3=c, se ele for o primeiro da lista, todo o resto apos ele tem de ser nomeado tambem, se ele for o ultimo não, e tudo que vem apos o nome se chama argumento nome3 -> nome do parametro e c -> argumento do parametro.