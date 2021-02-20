'''Faça um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa devera pergutnar se o
usuario quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos
B)Quantos homens foram cadastrados
C) Qauntas mulheres tem menos de 20 anos'''

print('--'*15)
print('CADASTRE UMA PESSOA')
print('--'*15)

soma = homem = mulher = 0

while True:
    idade = int(input('Digite sua idade: '))
    continuar = ' '

    while continuar not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
        break
    if idade >= 18:
        soma += 1
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher += 1

    decisao = ' '
    while decisao not in 'SN':
        decisao = str(input('Você quer continuar [S/N]? ')).strip().upper()[0]
    if decisao == 'N':
        break

print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {soma}')
print(f'Ao todo temos {homem} homem cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')