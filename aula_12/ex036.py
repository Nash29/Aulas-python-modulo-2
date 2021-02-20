# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar
# o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo sera negado

casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o seu salario: '))
ano = int(input('Em quantos anos deseja pargar: '))
prestacao = casa / (ano * 12)
minimo = sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de {:.2f}'.format(casa, ano, prestacao))

if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')
