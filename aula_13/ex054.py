# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoa
# ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
data_atual = date.today().year

totmaior = 0
totmenor = 0
for pess in range(7):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess+1)))
    idade = data_atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))
