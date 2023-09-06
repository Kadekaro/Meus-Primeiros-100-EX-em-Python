media = 0
contador = 0
a = ''.split()
x = 0
while x != 'n':
    b = float(input('Digite um numero para somá-lo: '))
    a.append(b)
    media += b
    contador += 1
    a.sort()
    x = input('Você quer digitar outro valor e somá-lo?(Digite (s) para sim, e (n) para não) R: ').lower().strip()[0]
    if x == 'n':
        print('\nMuito obrigado!\nO menor número que digitou é  o {}\nO maior número que digitou é o {}\n'
              'E a media entre os números digitados será de {}!'.format(a[0], a[-1], media / contador))
print('Volte sempre FIM!')
