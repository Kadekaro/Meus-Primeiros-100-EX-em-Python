import math
cat_op = float(input('Digite o cateto oposto: '))
cat_adj = float(input('Digite o cateto adjacente: '))
hip = math.hypot(cat_op, cat_adj)
print('A hipotenusa do triângulo será {:.2f}'.format(hip))
