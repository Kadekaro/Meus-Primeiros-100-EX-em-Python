print('-'*80)


def ficha(nome, gols):
    global name
    if goals >= 0:
        print(f'O jogador {nome} fez {gols} gols no campeonato!')
    return ficha


# programa principal
name = str(input('Nome do jogador: ')).strip().capitalize()
goals = str(input('Número de gols no campeonato: ')).strip()
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0
if name == '':
    name = '<desconhecido>'
ficha(name, goals)
