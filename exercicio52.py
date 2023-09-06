num = int(input('Digite um número inteiro para verificar se ele é primo: '))
divisiveis = 0
for x in range(1, num + 1):
    if num % x == 0:
        divisiveis += 1
print('O número {} foi dividido {} vezes'.format(num, divisiveis))
if divisiveis == 2:
    print('Esse número é primo!')
else:
    print('Esse número não é primo!')

