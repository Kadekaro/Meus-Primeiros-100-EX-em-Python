from random import randint
from time import sleep
numeros = list()
print(f'Sorteando 5 valores da lista: ', end='')


def sorteio(lista):
    for x in range(0, 5):
        y = randint(0, 20)
        print(f'{y} ', end='', flush=True)
        lista.append(y)
        sleep(1)
    print('PRONTO!')


def somaPar(lista):
    sp = 0
    for num in lista:
        if num % 2 == 0:
            sp += num
    print(f'Somando os valores pares de {lista}, temos {sp}!')


sorteio(numeros)
somaPar(numeros)
