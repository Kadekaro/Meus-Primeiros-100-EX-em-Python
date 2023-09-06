lista = [[], []]
for p in range(0, 7):
    x = float(input(f'Digite o {p+1}º número: '))
    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)
print('=-'*30)
a = sorted(lista[0])
print(f'Os valores pares digitados foram {a}!')
b = sorted(lista[1])
print(f'Os valores ímpares digitados foram {b}!')


