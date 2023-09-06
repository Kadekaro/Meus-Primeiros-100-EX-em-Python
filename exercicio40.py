a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
media = (a + b) / 2
if media < 5:
    print('Reprovado! E a sua média é {:.1f}, estude mais otário!'.format(media))
elif media <= 6.9:
    print('Você está de recuperação e a sua média é {:.1f}!'.format(media))
else:
    print('\033[31mParabéns!\033[m \033[34mVocê foi aprovado e a sua '
          'média é {}{:.1f}{}\033[34m!'.format('\033[31m', media, '\033[m'))
