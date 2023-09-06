from random import randint
y = randint(0, 10)
print('Olá eu sou seu computador e pensei em um número entre 0 e 10!')
print('Tente adivinhá-lo se for capas HAHAHA!')
palpites = 0
acertou = False
print('\033[31mPROCESSANDO...\033[m')
while not acertou:
    jogador = int(input('Digite um número entre 0 e 10: '))
    palpites += 1
    if jogador == y:
        acertou = True
    else:
        if jogador < y:
            print('Tente novamente jogando um número mais alto!')
        elif jogador > y:
            print('Tente novamente jogando um número mais baixo')
print('Parabéns você acertou depois de {} tentativas!'.format(palpites))

