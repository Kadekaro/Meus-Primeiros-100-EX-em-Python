a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))
if a < b:
    print('O valor {:.2f} é menor que o valor {:.2f}'.format(a, b))
elif a > b:
    print('O valor {:.2f} é maior que o valor {:.2f}'.format(a, b))
else:
    print('O valor {:.2f} e o valor {:.2f} são iguais'.format(a, b))
