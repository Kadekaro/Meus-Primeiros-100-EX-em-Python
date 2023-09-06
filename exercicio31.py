distancia = float(input('Qual a distância que você viajou em km? R: '))
preço_200km = distancia * 0.5
preço_maior_200km = distancia * 0.45
if distancia <= 200:
    print('Você pagará R${:.2f} na passagem'.format(preço_200km))
else:
    print('Você pagará R${:.2f} na passagem'.format(preço_maior_200km))

