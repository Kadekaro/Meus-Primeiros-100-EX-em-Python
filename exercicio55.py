x = []
for peso in range(1, 6):
    p = float(input('Digite o peso da {}° pessoa: '.format(peso)))
    x.append(p)
    x.sort()
print('O de menor peso entre eles é o de: {:.2f} Kg'.format(x[0]))
print('O de maior peso entre eles é o de: {:.2f} Kg'.format(x[4]))
