# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: PLENO
# - Acima: SENIOR

from datetime import date

data = date.today().year

nasc = int(input('Digite a data de nascimento do atleta: '))
idade = data - nasc

if idade <= 9:
    print('Categoria Mirim')
elif idade <= 14:
    print('Categoria Infantil')
elif idade <= 19:
    print('Categoria Junior')
elif idade <= 20:
    print('Categoria Pleno')
else:
    print('Categoria Senior')
