# # Básico:

# # Imprimir uma mensagem:
# # Escreva um programa que imprima "Olá, Mundo!" na tela.
# # print('Olá, Mundo!')

# # Operações matemáticas:
# # Solicite dois números ao usuário e imprima a soma, subtração, multiplicação e divisão deles.

# # n = int(input('Insira um valor: '))
# # n2 = int(input('Insira outro valor: '))
# # soma = n + n2 
# # print('A soma de %i e %i é %i' % (n, n2, soma))

# # Par ou Ímpar:
# # Escreva um programa que leia um número e informe se ele é par ou ímpar.

# # n = int(input('Insira um número: '))
# # par = n % 2 == 0
# # print(f'O número {n} é PAR? {par}')

# # Lista de compras:
# # Crie um programa que permita ao usuário adicionar itens a uma lista de compras e, ao final, exiba a lista completa.

# print(6 * '-*-')
# print('LISTA DE COMPRAS')
# print(6 * '-*-')
# item_anterior = ''

# esc = input('Você quer acrescentar itens a sua lista? Sim ou Não: ').capitalize()
# if esc == 'Sim':
#     itens = str(input('Insira o item que você quer colocar: ')).capitalize()
#     lista_compras = []
#     lista_compras.append(itens)
#     lista_atualizada = lista_compras
#     print(f'Sua lista atual é {lista_atualizada}')
#     esc = input('Você quer acrescentar mais coisas? Sim ou Não: ').capitalize()
#     while esc == 'Sim':
#         itens = input('Insira o item que você quer colocar: ').capitalize()
#         lista_compras.append(itens)
#         lista_atualizada = lista_compras
#         print(f'Sua lista atual é {lista_atualizada}')
#         esc = input('Você quer acrescentar mais coisas? ').capitalize()
#         penultimo_item = lista_atualizada[:-1]
#         if penultimo_item[-1] == itens:
#             print('O item inserido já foi inserido anteriormente')
#             print('Iremos fazer a remoção do item para não ocorrer confusão.')
#             del lista_atualizada[-1]
#             print(f'A lista após a remoção do item é a seguinte {lista_atualizada}')
#     else:
#         print('Sua escolha foi diferente de SIM, você saiu do loop para fazer sua lista de compra')
# else:
#     print(f'Sua escolha foi {esc}')
            

try:
    value = input('Entre um valor: ')
    print(value/value)
except ValueError:
    print('Entrada incorreta')
except ZeroDivisionError:
    print('Entrada muito ruim')
except TypeError:
    print('Muito ruim ruim entrada')
except:
    print('Boo!')