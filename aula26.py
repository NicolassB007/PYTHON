'''
Formatações básicas de strings
s - string
d - int 
f - float 
.<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(Quantidade)
> - esquerda
< - direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversation flags - !r !s !a __repr__ __str__ __asc__

'''

variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{100000.4184142:0=+,.2f}')
print(f'O hexadecimal de 1500 é {1500:08x}')