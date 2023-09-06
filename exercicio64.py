'''x = contador = somador = 0
a = 999
while contador != a:
    if x == 999:
        print('Você digitou {} números e a soma entre eles é de {:.2f}!'.format(contador - 1, somador - a))
        contador = a
    else:
        x = float(input('Digite vários números inteiros e [para sair digite o valor 999]: '))
        somador += x
        contador += 1'''

# Jeito do Guanabara abaixo \/

núm = cont = soma = 0
núm = float(input('Digite um número ou [999 para sair]: '))
while núm != 999:
    cont += 1
    soma += núm
    núm = float(input('Digite um número ou [999 para sair]: '))
print('Você digitou {} números e a soma entre eles é de {}'.format(cont, soma))
