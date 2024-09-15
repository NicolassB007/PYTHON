a = 'AAAAAAA'
b = 'B'
c = 1.1
string = 'a={nome1} a={nome1} a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c) # nome3 é um parâmetro

print(formato)

nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))




