'''Faça um prorama que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
Caso esteja errado, peça a digitação novamente até ter um valor correto'''

sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]

while sexo not in 'MF':
    sexo  = str(input('Dados Invalidos. Por favor, informe seu sexo: ')).upper().split()[0]
print('Sexo {} resgitado com sucesso'.format(sexo))
