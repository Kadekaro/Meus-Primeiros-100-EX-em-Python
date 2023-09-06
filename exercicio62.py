a = int(input('Digite o primeiro termo de uma p.a: '))
r = int(input('Digite a razão dessa p.a: '))
contador = 1
acumulador = a
x = int(input('Que termo quer mostrar? R: '))
while contador <= x:
    print(' -> {}'.format(acumulador), end='')
    print('.' if contador == x else '', end='')
    acumulador += r
    contador += 1
print('\n')
termo = input('Quer mostrar mais algum termo? (sim(s)/não(n)) R: ').lower().strip()[0]
while termo == 's':
    termo = int(input('Digite o outro termo: '))
    if termo < x:
        print('Esse valor já foi mostrado olhe a cima!')
    while contador <= termo:
        print(' -> {}'.format(acumulador), end='')
        print('.' if contador == termo else '', end='')
        acumulador += r
        contador += 1
    termo = input('\nQuer mostrar mais algum termo? (sim(s)/não(n)) R: ').lower().strip()[0]
else:
    y = int(input('Digite 0 para sair: '))
    if y == 0:
        print('Obrigado!')

