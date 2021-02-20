'''Melhore o DESAFIO 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa
encerra qunado ele disser que quer mstrar 0 termos'''

print('=-'*10)
print('10 TERMOS DE UMA PA')
print('=-'*10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Prograssão finalizada com {} termos mostrados.'.format(total))
print('FIM')
