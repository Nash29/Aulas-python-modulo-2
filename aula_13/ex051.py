# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa prograssão // ex: 1 até 100 pulando de 10 em 10

print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)

p1 = int(input('Digite o primeiro termo: '))
R = int(input('Digite a razão: '))
decimo = p1 + (10 - 1) * R

for i in range(p1, decimo + R, R):
    print('{}'.format(i), end=' -> ')
print('ACABOU')
