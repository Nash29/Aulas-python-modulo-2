# Crie um programa que faça o computador jogar JOKENPÔ com você

import random
from time import sleep

print('-='*15)
print('           JOKENPÔ      ')
print('-='*15)

itens = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0, 2)

print('Suas opções:')
print('\033[32m[ 0 ] PEDRA\033[m')
print('\033[35m[ 1 ] PAPEL\033[m')
print('\033[36m[ 2 ] TESOURA\033[m')

player = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('-='*15)
print('Computador jogou {}'.format(itens[pc]))
print('Player jogou {}'.format(itens[player]))
print('-='*15)

if pc == 0:# Computador jogou PEDRA
    if player == 0:
        print('\033[33mEMPATE\033[m')
    elif player == 1:
        print('\033[34mVOCÊ VENCEU\033[m')
    elif player == 2:
        print('\033[31mCOMPUTADOR VENCEU\033[m')
    else:
        print('JOGADA INVALIDA!')
elif pc == 1:# Computador jogou PAPEL
    if player == 0:
        print('\033[31mCOMPUTADOR VENCEU\033[m')
    elif player == 1:
        print('\033[33mEMPATE\033[m')
    elif player == 2:
        print('\033[34mVOCÊ VENCEU\033[m')
    else:
        print('JOGADA INVALIDA!')
elif pc == 2:# Computador jogou TESOURA
    if player == 0:
        print('\033[34mVOCÊ VENCEU\033[m')
    elif player == 1:
        print('\033[31mCOMPUTADOR VENCEU\033[m')
    elif player == 2:
        print('\033[33mEMPATE\033[m')
    else:
        print('JOGADA INVALIDA!')