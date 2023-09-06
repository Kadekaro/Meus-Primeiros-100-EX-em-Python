n1 = float(input('\033[1;34mDigite sua nota: \033[m'))
n2 = float(input('\033[1;34mDigite sua outra nota: \033[m'))
media = (n1 + n2)/2
print('\033[1;34mA sua média será: {}{:.2f}{}\033[1;34m!\033[m'.format('\033[4;31m', media, '\033[m'))

