soma = 0
cont = 0
for x in range(1, 7):
    n = float(input('Digite um número para somar seu valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
    else:
        print('Todos os valores ímpares serão desconsiderados, digite só valores pares por gentileza!')
print('A soma dos {} número(s) PARES digitados será de {}'.format(cont, soma))
