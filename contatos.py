"""
Gabriel Bitencourt Marin - UTF-8 - PT-BR
projAgenda 23-04-2022
"""

nomes = []
emails = []
telefones = []
valor_hora = []

resposta = ''
contatos = 0
print('Bem vindo ao projAgenda!')
while True:
    print('='*50)
    print('1 - Criar contato')
    print('2 - Mudar contato')
    print('3 - Excluir contato')
    print('4 - Consultar contatos')
    print('0 - Sair')
    resposta = input('Escolha uma das opções acima: ')
    print('-'*50)

    if resposta == '0':
        print('Sair')
        break

    elif resposta == '1':
        print('Criar')
        nomes.append(input('Digite o nome do contato: '))
        emails.append(input('Digite o e-mail do contato: '))
        telefones.append(input('Digite o telefone do contato: '))
        valor_hora.append(input('Digite o valor-hora do contato: R$ '))
        contatos += 1
    
    elif resposta == '2':
        print('Mudar')
        pass

    elif resposta == '3':
        print('Excluir')
        pass

    elif resposta == '4':
        print('Consultar')
        print('='*50)
        print('índice | nome | email | telefone | valor-hora')
        print('-'*50)
        for contato in range(contatos):
            print(f'{contato} | {nomes[contato]} | {emails[contato]} | {telefones[contato]} | R$ {valor_hora[contato]}')
        print('-'*50)
        input('Pressione <Enter> para continuar...')

    else:
        print('Digite uma das opções acima!')
