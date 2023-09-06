ladoA = float(input('Digite o lado A: '))
ladoB = float(input('Digite o lado B: '))
ladoC = float(input('Digite o lado C: '))
triangulo = ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoB + ladoA
if triangulo is True:
    print('Os valores {}, {}, {} formam um \033[31mTRIÂNGULO!\033[m'.format(ladoA, ladoB, ladoC))
    if ladoA == ladoB == ladoC:
        print('Esse triângulo é \033[31mEQUILÁTERO!')
    elif ladoB == ladoA or ladoA == ladoC or ladoC == ladoB:
        print('Esse triângulo é \033[31mISÓSCELES!')
    else:
        print('Esse triângulo é \033[31mESCALENO!')
else:
    print('Os valores {}, {}, {} não formam um triângulo!'.format(ladoA, ladoB, ladoC))

