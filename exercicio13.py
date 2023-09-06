salario = float(input('\033[34mDigite seu salário em R$: '))
salario_com_aumento = salario + (salario*0.15)
print('Seu novo salário será de\033[m {}R${:.2f}{}!'.format('\033[4;31m', salario_com_aumento, '\033[m'))
