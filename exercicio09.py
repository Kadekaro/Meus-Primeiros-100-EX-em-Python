n = int(input('\033[1;31mDigite um número: \033[m'))
tabuada = 1
for tabuada in range(1, 11):
    print('{}{} * {:2}{}={} {} {}'.format('\033[34m', n, tabuada, '\033[m', '\033[31m', n * tabuada, '\033[m'))
tabuada = 1
for tabuada in range(1, 10):
    print(n*tabuada)

# AGORA IREI FAZER COM O COMANDO WHILE

n = int(input('Digite um número: '))
contador = 1
while contador <= 10:
    n1 = n * contador
    print('{} * {:2} = {}'.format(n, contador, n1))
    contador += 1
