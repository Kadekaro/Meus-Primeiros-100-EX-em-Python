a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
if a < b and a < c:
    print('O menor número é o {}'.format(a))
elif b < c:
    print('O menor número é o {}'.format(b))
else:
    print('O menor é o número {}'.format(c))

if a > b and a > c:
    print('O maior número é o {}'.format(a))
elif b > c:
    print('O maior número é o {}'.format(b))
else:
    print('O maior número é o {}'.format(c))
