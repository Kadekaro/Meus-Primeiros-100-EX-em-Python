print('    Controle de terreno!'.upper())
print('-'*60)
def area(L , C):
    a = L * C
    print(f'A área de um terreno {L:.2f} x {C:.2f} é de = {a:.2f}m².')

area((float(input('Digite o valor da largura do terreno em metros: '))),
    (float(input('Digite o valor do comprimento do terreno em metros: '))))

