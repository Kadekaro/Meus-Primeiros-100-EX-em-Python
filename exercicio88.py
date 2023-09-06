from random import randint
from time import sleep
print('-'*60)
print('{:>35}'.format('joga na mega sena').upper())
print('-'*60)
lista = []
jogos = []
x = int(input('Quantos jogos você quer que eu sorteie? '))
print()
print('=-'*3, f'SORTEANDO {x} JOGOS', '=-'*3)
print()

for i in range(0, x):
    for c in range(0, 6):
        y = randint(1, 60)
        if y not in jogos:
            jogos.append(y)
        else:
            y = randint(1, 60)
            jogos.append(y)
    jogos.sort()
    lista.append(jogos[:])
    jogos.clear()

for rodada, jogada in enumerate(lista):
    print(f'JOGO {rodada + 1}: {jogada}')
    sleep(1)
    print()
print()
print('=-'*5, 'BOA SORTE', '=-'*5)
