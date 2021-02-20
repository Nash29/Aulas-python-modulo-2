# Faça o DESAFIO 009, mostrando a tabuada de um numero que o usuario escolher, só que agora
# utilizando um laço for

num = int(input('Digite um numero: '))

for i in range(10+1):
    print('{} X {:2} = {}'.format(num, i, num*i))
