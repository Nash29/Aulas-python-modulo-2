'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em im NUMERO ENTRE 0 E 10
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessarios para vencer'''

import random
computador = random.randint(0, 10)

print('Sou seu computador acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi? ')
palpites = 0
acertou = False
while not acertou:
    player = int(input('Qual é o seu palpite? '))
    palpites += 1
    if player == computador:
        acertou = True
    else:
        if player < computador:
            print('Mais... Tente mais uma vez.')
        elif player > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou! Com {} tentativas'.format(palpites))
