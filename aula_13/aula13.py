for i in range(6, 0, -1):
    print(i)
print('fim')

n = int(input('Digite um numero: '))
for i in range(n+1):
    print(i)

s = 0
for i in range(4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))