times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
         'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba',
         'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-='*60)
print(f'Lista de times do Brasileirão 2018: {times}')
print('-='*60)
print(f'Os 5 primeiros colocados são: {times[0: 5]}')
print('-='*60)
print(f'Os últimos 4 colocados da tabela são: {times[-4:]}')
print('-='*60)
print('Times em ordem alfabéticas: ', sorted(times))
print('-='*60)
lugar = times.index('Chapecoense') + 1
print(f'O CHAPECOENSE está na {lugar}° posição')
print('-='*60)