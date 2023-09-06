def leiaint(i):
    x = str(input(i)).strip()
    while True:
        if x.isnumeric():
            y = int(x)
            print(f'Você acabou de digitar o número {y}!')
            break
        else:
            print(f'\033[4;31mErro! Digite um número inteiro válido.\033[m')
            x = str(input(i)).strip()


# programa principal
leiaint('Digite um n°: ')