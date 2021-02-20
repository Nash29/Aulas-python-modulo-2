# Faça um programa que leia um número inteiro e diga se ele é ou não um numero primo //Divisivel por um e por ele mesmo

num = int(input('Digite um número: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:#Mostra por quais numeros ele foi divido
        print('\033[33m', end='')#Amarelo
        tot += 1# Soma pela quantidade de numero que pode ser dividido
    else:# Mostra por quais numero ele NÃO foi dividido
        print('\033[31m', end='')#Vermelha
    print('{} '.format(i), end='')# mostra os numeros

print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é primo!')
