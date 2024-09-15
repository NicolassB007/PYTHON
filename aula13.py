nome = 'Nicolas'
altura = 1.80
peso = 95
imc = peso / (altura ** 2)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'E pesa {peso}, seu IMC é de {imc:.2f}'

print(linha_1)
print(linha_2)
