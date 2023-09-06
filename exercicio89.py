lista = []
pessoas = []
while True:
    pessoas.append(str(input('Nome? R: ').capitalize()))
    pessoas.append(float(input('Nota 1? R: ')))
    pessoas.append(float(input('Nota 2? R: ')))
    lista.append(pessoas[:])  # <<< o colchete e os dois pontos fazem muita diferença fique atento.
    pessoas.clear()
    pergunta = str(input('Quer continuar [S/N]? R: ')).upper().strip()[0]
    if pergunta == 'N':
        break
print('-='*30)
print(f'{"Nº":<6}', f'{"Nome":<12}', f'{"Média":>21}')
print('-'*60)
for c, i in enumerate(lista):
    media = (i[1] + i[2]) / 2
    print(f'{c+1:<6}', f'{i[0]:<15}', f'{media:>18.1f}')
print('-'*60)
while True:
    x = int(input('Mostrar notas de qual aluno? (Digitar 999 interrompe!) R: '))
    for c, i in enumerate(lista):
        if x == (c+1):
            print(f'As notas de {i[0]} são [{i[1]}, {i[2]}]')
    if x == 999:
        break
print('FINALIZANDO...')
print(f'{"<<< VOLTE SEMPRE  >>>":>40}')