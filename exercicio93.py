jogador = {}
gols = []
soma = cont = 0
jogador['Nome do Jogador'] = str(input('Digite o nome do jogador: ')).capitalize()
partidas = int(input(f"Quantas partidas {jogador['Nome do Jogador']} jogou: "))
while cont < partidas:
    y = int(input(f'Quantos gols na partida {len(gols)+1}º: '))
    gols.append(y)
    soma += y
    cont += 1
jogador['Gols'] = gols[:]
jogador['Total de Gols'] = soma
print('=-'*50)
print(jogador)
print('=-'*50)
for k, v in jogador.items():
    print(f'{k} tem valor {v}')
print('=-'*50)
print(f"O jogador {jogador['Nome do Jogador']} jogou {partidas} partidas.")
for k, v in enumerate(gols):
    print(f'     => Na {k + 1}º partida , fez {v} gols.')
print(f'Foi um total de {soma} gols.')
