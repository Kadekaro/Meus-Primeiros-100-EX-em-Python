altura = float(input('\033[34mDigite a altura da parede em metros: \033[m'))
largura = float(input('\033[34mDigite a largura da parede em metros: \033[m'))
area = altura * largura
litros_de_tinta = area / 2
print('\033[34mVocê vai precisar de{} {:.2f} {}\033[34mlitros de tinta!\033[m'.format('\033[4;31m', litros_de_tinta, '\033[m'))
