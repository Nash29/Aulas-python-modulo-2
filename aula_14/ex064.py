'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuario digitar o valor 999, que é a condição do programa. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag = 999)'''

valor = quantidade = soma = 0

while valor != 999:
    valor = int(input('Digite um número [999 para parar]: '))
    if valor != 999:
        quantidade += 1
        soma += valor

print('Você digitou {} números e a soma entre eles foi {}'.format(quantidade, soma))
print('Fim')
