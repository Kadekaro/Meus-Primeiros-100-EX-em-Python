from random import randint
from time import sleep
from operator import itemgetter

jogador = {'Jogador(1)': randint(1, 6),
           'Jogador(2)': randint(1, 6),
           'Jogador(3)': randint(1, 6),
           'Jogador(4)': randint(1, 6)}

ranking = {}
print(f'VALORES SORTEADOS:')
for k, v in jogador.items():
    print(f'{f"O {k}, tirou -> {v}!":>30}')
    sleep(1)

ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)


print('=-'*30)
print(f'         == RANKING DOS JOGADORES ==')

for k, v in enumerate(ranking):
    print(f'          {k+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

print('=-'*30)

