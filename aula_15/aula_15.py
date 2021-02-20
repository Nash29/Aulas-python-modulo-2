'''n = soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
#print('A soma vale {}'.format(soma))
print(f'A soma vale {soma}')'''

nome = 'José'
idade = 33
salario = 987.35467
print(f'O {nome:^20} tem {idade} anos e ganha R${salario:.2f}')
