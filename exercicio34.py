salario = float(input('Digite o seu salário em R$:'))
aumento_maior_1250 = salario * 0.1
aumento_menor_1250 = salario * 0.15
if salario > 1250:
    print('Seu aumento foi de R$ {:.2f} e seu novo salario é R$ {:.2f}'.format(aumento_maior_1250, salario + aumento_maior_1250))
else:
    print('Seu aumento foi de R$ {:.2f} e seu novo salario é R$ {:.2f}'.format(aumento_menor_1250, salario + aumento_menor_1250))
