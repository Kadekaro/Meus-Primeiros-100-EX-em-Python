ladoA = float(input('Digite o lado A: '))
ladoB = float(input('Digite o lado B: '))
ladoC = float(input('Digite o lado C: '))
if ladoA < ladoB + ladoC and ladoB < ladoA + ladoB and ladoC < ladoB + ladoA:
    print('Os valores {}, {}, {} formam um triângulo'.format(ladoA, ladoB, ladoC))
else:
    print('Os valores {}, {}, {} não formam um triângulo'.format(ladoA, ladoB, ladoC))
