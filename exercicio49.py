n = int(input('Digite um número inteiro para ver sua tabuada de 0 a 10: '))
for x in range(0, 11):
    print('{} x {:2} = {}'.format(n, x, n*x))

