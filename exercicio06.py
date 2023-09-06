n = int(input('\033[1;34mDigite um número: \033[m'))
n1 = n * 2
n2 = n * 3
n3 = n ** (1/2)
print('\033[1;34mO dobro do número digitado será\033[m \033[1;31m{}\033[m \033[1;34m, o seu triplo será\033[m \033[1;31m{}\033[m'.format(n1, n2), end='\033[1;34m, \033[m')
print('\033[1;34msua raiz quadrada será\033[m \033[1;31m{}\033[m'.format(n3))

