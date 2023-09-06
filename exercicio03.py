n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
d = n1 - n2
m = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
potencia = n1 ** n2
raiz_quadrada = n1

print('{} + {}  = {}'.format(n1, n2, s))
print('{} - {}  = {}'.format(n1, n2, d))
print('{} * {}  = {}'.format(n1, n2, m))
print('{} / {}  = {:.2f}'.format(n1, n2, divisao))
print('{} // {}  = {}'.format(n1, n2, divisao_inteira))
print('{} ** {}  = {}'.format(n1, n2, potencia))

