from datetime import date
x = int(input('Digite um ano para verificar se ele é bissexto: '))
if x == 0:
    x = date.today().year
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print('{} é um ano bissexto'.format(x))
else:
    print('{} não é um ano bissexto'.format(x))
