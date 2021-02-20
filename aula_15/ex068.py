'''Faça um programa que jogue par ou impar com o computador. O jogo só sera interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo
in = Estiver
not in = Não estiver '''
import random

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

v = 0

while True:
    jogador = int(input('Digite um valor: '))
    pc = random.randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]?')).strip().upper()[0] #Tira os espaços, deixa tudo MAIUSCULO e pega a primeira letra
    print(f'Você jogou {jogador} e o computador {pc}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
