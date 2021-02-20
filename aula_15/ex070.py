'''Crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuario vai continuar.
No final, mostre:
A) Qual é o total gasto na compra
B) Qauntos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato'''

print('--' * 15)
print('      LOJA SUPER BARATAO')
print('--' * 15)

soma = quantidade = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    decisao = ' '
    novonome = ' '
    soma += preco
    cont += 1
    if preco > 1000:
        quantidade += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    while decisao not in 'SN':
        decisao = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if decisao == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {quantidade} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
