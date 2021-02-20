# Elabore um programa que calcule o valor a ser pago por um produtp, considerando o seu preço normal e consição de pagamento:
# A vista dinheiro/cheque: 10% de desconto
# A vista no Cartão: 5% de desconto
# Em até 2x no catão: Preço Normal
# 3x ou mais no cartão: 20% de juros

valor = float(input('Digite o valor do produto: '))
print('Opções de pagamento')
print('1 - 10% de desconto a vista no dinheiro/cheque')
print('2 - 5% de desconto a vista no Cartão')
print('3 - Em até 2x no Cartão, preço da etiqueta')
print('4 - 3x ou mais no cartão 20% de juros')

op = int(input('Digite a opção de pagamento: '))

if op == 1:
    print('Você tera que pagar R${:.2f}'.format(valor-(valor*10)/100))
elif op == 2:
    print('Você tera que pagar R${:.2f}'.format(valor-(valor*5)/100))
elif op == 3:
    print('Você tera que pagar {} parcelas de {:.2f} por mês'.format(2, valor/2))
elif op == 4:
    par = int(input('Digite em quantas parcelas você vai pagar: '))
    print('Você tera que pagar {} parcelas de {} por mês'.format(par, (valor+((valor*20)/100))/par))
