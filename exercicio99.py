from time import sleep


def contador(*num):
    cont = maior = 0
    print('-=' * 50)
    print(f'Analisando os valores passados... ')
    sleep(2)
    y = len(num)
    if cont <= len(num):
        for x in num:
            print(f'{x} ', end='')
            sleep(0.5)
            cont += 1
            if cont == 0:
                maior = x
            else:
                if x > maior:
                    maior = x
        sleep(1)
        print(f'foram informados {y} valores ao todo!')
        sleep(1)
        print(f'O maior valor informado foi o {maior}!')



#programa principal
contador(2)
contador(1, 5, 3, 8)
contador(3, 5, 9, 63, 40)
contador(34, 56, 23, 90, 5, 32)
contador()
