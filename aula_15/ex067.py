'''Faça um programa que mostra a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuario.
O programa será interrompido quando o numero solicitados for negativo
ex: print("Voc equer ver a tabuada de qual valor? ")
 se numero for negativo Programa encerrado'''

valor = 0
while True: #Looping infinito
    print('-'*30)
    valor = int(input('Você quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if valor < 0:
        break
    for i in range(10+1):
        print(f'{valor} X {i:2} = {valor*i}')

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
