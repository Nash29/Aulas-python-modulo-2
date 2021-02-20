# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilatero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

print('-='*20)
print('Analizador de Triângulo')
print('-='*20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')

if r1 == r2 == r3:
    print('É um triângulo EQUILATERO')
elif r1 == r2 or r2 == r3 or r3 == r1:
    print('É um triângulo ISÓSCELES')
else:
    print('É um triângulo ESCALENO')
