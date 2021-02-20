'''Faça um programa que leia um número qualquer e mostre o seu fatorial
Ex: 5! = 5x4x3x2x1 = 120
'''

# PRIMEIRA OPÇÃO:  IMPORTANDO O FATORIAL
'''import math
n = int(input('Digite um número para calcular seu Fatorial: '))
f = math.factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''

# SEGUNDA OPÇÃO: FAZENDO NA MÃO

n = int(input('Digte um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
