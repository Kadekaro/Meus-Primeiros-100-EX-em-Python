a1 = int(input('Digite o primeiro termo da p.a: '))
r = int(input('Digite a razão dessa p.a: '))
soma = a1
for x in range(1, 11):
    print('O {}º termo é {}'.format(x, soma), end=' -> ')
    soma += r
print('Fim')
'''a = int(input('Digite o primeiro termo de uma p.a: '))
r = int(input('Digite a razão dessa p.a: '))
b = int(input('Digite até qual termo deseja saber a p.a: '))
contador = 1
acumulador = a
while contador <= b:
    print('O {}º termo é {}'.format(contador, acumulador), end='')
    print(' -> ' if contador != b else '.', end='')
    acumulador += r
    contador += 1'''
