import math
angulo = int(input('Digite um ângulo: '))
print('O seno será de {:.2f}, o coseno será de {:.2f} e a tangente será de {:.2f}'.format(math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))

# quando o phyton calcula o valor do seno coseno e tangente ele tras o valor em radianos, você tem que que converter o valor do radiano do angulo em valor de medida!