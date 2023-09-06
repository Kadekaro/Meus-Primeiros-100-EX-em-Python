peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Seu imc é {:.2f} e você está abaixo do peso!'.format(imc))
elif imc <= 25:
    print('Seu imc é {:.2f} e você está com um peso ideal!'.format(imc))
elif imc <= 30:
    print('Seu imc é {:.2f} e você está com sobrepeso!'.format(imc))
elif imc <= 40:
    print('Seu imc é {:.2f} e você é uma pessoa obesa!'.format(imc))
else:
    print('Seu imc é {:.2f} e você possui obesidade mórbida!'.format(imc))
