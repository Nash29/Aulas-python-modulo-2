# Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual sera a base de conversão
# -1 para binario
# -2 para octal
# -3 para hexadecimal

n1 = int(input('Digite um número: '))
binario = bin(n1)
hexadecimal = hex(n1)
octal = oct(n1)
print('O número {} em binario é {}'.format(n1, binario))
print('O número {} em hexadecimal é {}'.format(n1, hexadecimal))
print('O número {} em octal é {}'.format(n1, octal))
