'''
Interpolação básica de strings

s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)

'''

nome = 'Nicolas'
preco = 1000.95897643
variavel = '%s, o preço total foi R$%.2f' % (nome, preco )
print(variavel)
print('O hexadecimal de %d é %04x' % (15, 15)) 
