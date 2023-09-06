'''x = int(input('Digite um número inteiro para ver seu fatorial: '))
mult = x
fat = 1
print('Calculando {}! = '.format(x), end='')
while mult > 0:
    print('{} '.format(mult), end='')
    print('x ' if mult > 1 else '=', end='')
    fat = fat * mult
    mult -= 1
print(' é {}.'.format(fat))'''


x = int(input('Digite um valor para ver seu fatorial: '))
fat = 1
print('O fatorial de {}! é >>>'.format(x), end='')
for b in range(x, 0, -1):
    print(' {}'.format(b), end='')
    print(' = ' if b == 1 else ' x', end='')
    fat *= b
print('{}.'.format(fat))
