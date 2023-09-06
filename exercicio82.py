impar = []
par = []
lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    elif num % 2 != 0:
        impar.append(num)
    y = input('Quer continuar: (S/N): ').upper().strip()[0]
    if y == 'N':
        print('=-'*30)
        print(f'A lista completa é {lista}')
        print(f'Os números pares da lista são {par}')
        print(f'Os números impares da lista são {impar}')
        break
