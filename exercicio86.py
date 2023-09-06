matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(matriz)):
    for p in range(len(matriz)):
        matriz[i][p] = int(input(f'Digite o valor {i, p} da matriz: '))
print('=-'*40)
for i in range(len(matriz)):
    for p in range(len(matriz)):
        print(f'[{matriz[i][p]:^5}]', end='')
    print()
