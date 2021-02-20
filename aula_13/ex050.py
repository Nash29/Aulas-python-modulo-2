# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o

par = 0
val = 0
for i in range(6):
    num = int(input('Digite o {}° número inteiro: '.format(i+1)))
    if num % 2 == 0:
        par += num
        val += 1
print('O valor da soma dos {} números pares é {}'.format(val, par))
