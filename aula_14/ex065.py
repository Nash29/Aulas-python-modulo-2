'''Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a media entre todos os valores e qual
foi o maior e menor valores lidos. O programa deve pergutar ao usuario se ele quer ou não continuar a digitar valores'''

num = 0
r = 'S'
soma = quantidade = media = maior = menor = 0

while r == 'S':   #OU while r in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1

    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('Você deseja continuar [S/N]? ')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} números e a média foi {:.2f}'.format(quantidade, media))
print('O maior valor foi {} e o menor {}'.format(maior, menor))
