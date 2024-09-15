# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda expressão como verdadeira
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor
# 0 0.0 '' false 
# também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')
# senha_permitida = '123456'

# if True:
#    ...
# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else: 
#     print('Sair')

#Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)