m = int(input('\033[35mDigite um valor em metros: \033[m'))
cen = m * 100
mil = m * 1000
print('O valor em centímetros será de \033[31m {} \033[m centímetros, e o valor em milímetros será \033[31m {} \033[m milímetros'.format(cen, mil))

km = m / 1000
print('O valor em km será: \033[31m{}\033[m'.format(km))

