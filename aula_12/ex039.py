# Faça um programa que leia o ano de nascimento de um jovem e e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo

from datetime import date

data = date.today().year
nasc = int(input('Digite o ano em que você nasceu: '))
ano = data - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, ano, data))

if ano < 18:
    print('\033[7;30mAinda faltam {} anos para o alistamento\033[m'.format(18-ano))
    print('\033[34mSeu alistamento será em {}\033[m'.format(nasc+18))
elif ano == 18:
    print('\033[33mVocê tem que se alistar IMEDIATAMENTE\033[m!')
else:
    print('\033[1;41mVocê já deveria ter se alistado há {} anos\033[m'.format(ano-18))
    print('\033[31mSeu alistamento foi em {}\033[m'.format(nasc+18))





