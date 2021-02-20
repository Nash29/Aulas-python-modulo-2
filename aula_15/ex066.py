'''Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a consição de parada. No final, mostre quantos números foram deigitados e qual foi a soma entre eles
(descosiderando o flag)
print('Digite um valor (999 para parar')
ex: print(A soma dos 3 valores foi 12!)'''

num = soma = valor = 0

while True:
    num = int(input('Digite um numero (999 para parar): '))
    if num == 999:
        break
    soma += 1
    valor += num
print(f'A soma dos {soma} valores foi {valor}!')
