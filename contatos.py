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
while resposta.upper() == 'S' or resposta == '':
    while resposta.upper() not in ('S', 'N'):
        resposta = input('Deseja criar um novo contato? (S/N): ')
        if resposta.upper() not in ('S', 'N'):
            print('Não entendi a resposta, responda com "S" ou "N"!')
    
    if resposta.upper() == 'S':
        nomes.append(input('Digite o nome do contato: '))
        emails.append(input('Digite o e-mail do contato: '))
        telefones.append(input('Digite o telefone do contato: '))
        valor_hora.append(input('Digite o valor-hora do contato: R$ '))
        resposta = ''
        contatos += 1

print('='*20)
print('nome|email|telefone|valor-hora')
print('-'*20)
for contato in range(contatos):
    print(f'{nomes[contato]} | {emails[contato]} | {telefones[contato]} | R$ {valor_hora[contato]}')
