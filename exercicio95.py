jogador = {}
gols = []
time = []

while True:
    gols.clear()
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou: "))
    for a in range(partidas):
        y = int(input(f' - Quantos gols na {a + 1}º partida: '))
        gols.append(y)
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        x = input('Quer continuar[S/N]?').upper().strip()[0]
        if x in "SN":
            break
        print('Erro! Digite apenas [Sim] ou [Não]!')
    if x == 'N':
        print()
        break

print('-='*50)
print(f'Cod', end='   ')
for d, j in enumerate(jogador.keys()):
    print(f'{str(j):<19}', end='')
print()
print('-'*100)

for k, v in enumerate(time):
    print(f'{k:>2}', end='   ')
    for d in v.values():
        print(f'{str(d):<19}', end=' ')
    print()

print('=-'*50)
print()

while True:
    busca = int(input(f'Digite o Código(Cod) do jogador que você quer ver. Para sair digite [999]: '))
    if busca == 999:
        print('<< VOLTE SEMPRE >>')
        break
    if busca >= len(time):
        print('Opção invalida. Tente novamente.')
    else:
        print(f'--Levantamento do jogador {time[busca]["Nome"]}.')
        for k, v in enumerate(time[busca]["Gols"]):
            print(f'    {time[busca]["Nome"]} fez {v} gols na {k+1}º partida!')
        print(f'    Total de gols = {sum(time[busca]["Gols"])}.')
        print()
    print('-='*50)


