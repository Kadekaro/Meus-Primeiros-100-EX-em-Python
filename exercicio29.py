v = float(input('Digite a velocidade do carro em Km/h: '))
multa = (v - 80) * 7
if v > 80:
    print('Você foi multado e pagará R$:{:.2f}'.format(multa))
else:
    print('Você não foi multado, portanto não pagará nada!')

