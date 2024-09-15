nome = input('Insira seu nome completo: ')
idade = input('Insira sua idade: ')
contador_espacos = nome.count(' ')
contador_letras = len(nome)
if str(nome) and int(idade):
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if contador_espacos > 0:
        print(f'Seu nome tem {contador_espacos} espaços')

    else:
        print(f'Seu nome tem {contador_letras} letras')
        print(f'A primeira letra do seu nome é {nome[0]}')
        print(f'A última letra do seu nome é {nome[-1]}')
        
else:
    print('Você não inseriu os dados necessários!')
