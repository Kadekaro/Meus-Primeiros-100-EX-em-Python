from datetime import date
x = date.today().year
ano = int(input('Digite o ano que você nasceu no formato "aaaa": '))
idade = x - ano
if idade <= 9:
    print('Você está na categoria\033[34m MIRIM!')
elif idade <= 14:
    print('Você está na categoria\033[34m INFANTIL!')
elif idade <= 19:
    print('Você está na categoria\033[34m JUNIOR!')
elif idade <= 25:
    print('Você está na categoria\033[34m SÊNIOR!')
else:
    print('Você está na categoria\033[34m MASTER!')

