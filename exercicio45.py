from random import choice
from time import sleep
lista = ['PEDRA', 'PAPEL', 'TESOURA']
print('\033[31m-=-\033[m'*20)
print('\033[36mVocê consegue ganhar de mim no jokenpô?\033[m')
print('\033[31m-=-\033[m'*20)
x = input('\033[36mDigite "sim" para começarmos: \033[m').upper().strip()
if x == 'SIM':
    print('\033[31mComeçando...\033[m')
    sleep(2)
    b = choice(lista)
    y = input('\033[36mEscolha "PEDRA", "PAPEL" OU "TESOURA":\033[m ').upper().strip()
    print('JO')
    sleep(2)
    print('KEN')
    sleep(2)
    print('PÔ!')
    if y not in 'PEDRA PAPEL TESOURA':
        print('\033[1;31mPor favor escreva somente uma das 3 alternativas: "Pedra"; "Papel" ou "Tesoura"!\033[m')
        y = input('\033[36mEscolha "PEDRA", "PAPEL" OU "TESOURA":\033[m ').upper().strip()
        if y not in 'PEDRA PAPEL TESOURA':
            print('\033[1;31mReinicie o jogo se quiser jogar!\033[m')
        elif y != b:
            print('\033[31mInfelizmente você perdeu! Tente novamente!')
        else:
            print('\033[34mMeus parabéns você ganhou! Volte sempre!')
    elif y != b:
        print('\033[31mInfelizmente você perdeu! Tente novamente!')
    else:
        print('\033[34mMeus parabéns você ganhou! Volte sempre!')
else:
    print('\033[31mMuito obrigado, volte sempre!\033[m')
