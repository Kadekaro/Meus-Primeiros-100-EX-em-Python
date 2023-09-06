from time import sleep


def contador(inicio, final, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print('=-' * 50)
    print(f' Contagem de {inicio} a {final} de {passo} em {passo}: ')
    sleep(2)
    if inicio < final:
        cont = inicio
        while cont <= final:
            print(f'{cont:4}', end='', flush=True)   # pra mostrar cada print 1 a 1 por vez!
            sleep(0.5)
            cont += passo
        print(' Fim!')
    elif inicio > final:
        cont = inicio
        while cont >= final:
            print(f'{cont:4}', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print(' Fim!')
    print('=-'*50)


contador(1, 10, 1)
contador(10, 0, 2)

contador(int(input('   - Início: ')),
         int(input('   - Final: ')),
         int(input('   - Passo: ')))

