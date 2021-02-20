# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No fnal do programa, mostre:
# A media da idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher = 0
totMulher20 = 0

for i in range(4):
    print('----- {}° PESSOA -----'.format(i+1))
    nome = str(input('Digite seu nome: ')).strip()#tira os espaços
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip()#tira os espaços
    somaidade += idade
    mediaidade = somaidade/4

    if i == 0 and sexo in 'Mm':# O usuario pode colocar qualquer um dos Mm
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1

print('A média de idade do grupo é de {:.2f} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totMulher20))
