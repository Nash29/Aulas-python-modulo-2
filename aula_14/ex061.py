'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primerios termos da
prograssão usando a estrutura while'''

print('=-'*10)
print('10 TERMOS DE UMA PA')
print('=-'*10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')
