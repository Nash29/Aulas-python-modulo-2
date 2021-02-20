# Desenvolva um lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo
# com a tabela abaixo:
# Abaixo de 18.5: ABAIXO DO PESO
# Entre 18.5 e 25: PESO IDEAL
# 25 ate 30: SOBREPESO
# 30 ate 40: OBESIDADE
# Acima de 40: OBESIDADE MORBIDA

peso = float(input('Digite o seu peso: '))
alt = float(input('Digite a sua altura: '))
IMC = peso / (alt*alt)

if IMC < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= IMC < 25:
    print('PESO IDEAL')
elif 25 <= IMC < 30:
    print('SOBREPESO')
elif 30 <= IMC < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')
