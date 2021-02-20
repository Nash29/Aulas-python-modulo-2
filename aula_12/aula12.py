nome = str(input('\033[31mDigite seu nome: \033[m'))
if nome == 'Murilo':
    print('\033[35mQue nome bonito!\033[m')
elif nome == 'Natalia' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no brasil!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia {}{}{}'.format('\033[34m', nome, '\033[m'))
