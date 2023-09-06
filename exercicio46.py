from time import sleep
import emoji
a = '\033[31mA contagem final para os fogos começa agora: \033[m'
print('{:^110}'.format(a))
sleep(3)
for x in range(10, -1, -1):
    print('\033[34m{:^100}'.format(x))
    sleep(1)
b = '\033[1;32m:boom:Feliz ano novo!:boom:\033[m'
print('{:^110}'.format(emoji.emojize(b, use_aliases=True)))
