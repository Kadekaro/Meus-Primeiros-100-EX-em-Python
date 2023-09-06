#x = 0
#numero = ''.split()
#while x < 4:
#    y = input('Digite um número entre 0 e 9: ')
#    numero += y
#    x += 1
#print('Casa dos milhares = {}'.format(numero[0]))
#print('Casa das centenas = {}'.format(numero[1]))
#print('Casa das dezenas= {}'.format(numero[2]))
#print('Casa das unidades = {}'.format(numero[3]))

# << Por string o método não dá certo para número abaixo de 4 digitos do mesmo modo abaixo >>>

#numero = ''.split()
#x = input('Digite um número entre 1000 e 9999: ')
#numero.append(x)
#print('milhar = {}'.format(x[0]))
#print('centena = {}'.format(x[1]))
#print('dezenas= {}'.format(x[2]))
#print('unidade = {}'.format(x[3]))

# >>> Outra maneira de se fazer melhor que a segunda: <<<

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A unidade será: {}'.format(u))
print('A dezena será: {}'.format(d))
print('A centena será: {}'.format(c))
print('O milhar será: {}'.format(m))
