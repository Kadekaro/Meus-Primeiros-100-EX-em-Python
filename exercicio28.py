from random import randint
y = randint(0, 5)
x = int(input('Digite um número de 0 a 5: '))
print('\033[31mPROCESSANDO...\033[m')
print('Parabéns você venceu! Eu pensei no {} e você digitou o {}!'.format(y, x)
      if x == y else 'Infelizmente você perdeu, eu pensei no {} e não no {}!'.format(y, x,))

