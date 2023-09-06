matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
maior = 0
for i in range(len(matriz)):
    for p in range(len(matriz)):
        matriz[i][p] = int(input(f'Digite o valor {i, p} da matriz: '))
        if matriz[i][p] % 2 == 0:
            soma += matriz[i][p]
    if i == 1:
        maior = matriz[1][0]
    else:
        if matriz[1][p] > maior:
            maior = matriz[1][p]
print('=-'*40)
for i in range(len(matriz)):
    for p in range(len(matriz)):
        print(f'[{matriz[i][p]:^5}]', end='')
    print()
print(f'A soma de todos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')  # Eu fiz assim,
print(f'O maior número da segunda coluna é {maior}')                                            # mas do outro jeito
                                                                                                # abaixo é melhor!




''' outro método de fazer a soma da terceira coluna abaixo:                                       
somacoluna = 0    
for l in range(0, 3):
    somacoluna += matriz[l][2] 
print(f'A soma dos valores da terceira coluna é {somacoluna}')'''
