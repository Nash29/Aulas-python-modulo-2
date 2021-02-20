# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

n1 = float(input('\033[34mDigite o primeiro numero: \033[m'))
n2 = float(input('\033[31mDigite o segundo número: \033[m'))

if n1 > n2:
    print('O número {}{}{} é maior que o número {}{}{}'.format('\033[1;34m', n1, '\033[m', '\033[1;31m', n2, '\033[m'))
elif n2 > n1:
    print('O número {}{}{} é maior que o número {}{}{}'.format('\033[1;31m', n2, '\033[m', '\033[1;34m', n1, '\033[m'))
else:
    print('O número {}{}{} é igual ao número {}{}{}'.format('\033[1;34m', n2, '\033[m', '\033[1;34m', n1, '\033[m'))
