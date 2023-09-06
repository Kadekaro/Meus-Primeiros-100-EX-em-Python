x = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

y = int(input('Digite um número entre 0 e 20: '))

while y not in range(len(x)):
    print('Número inválido, tente novamente!', end='')
    y = int(input(' Digite um número entre 0 e 20: '))
print('Você digitou o número:', x[y])

while True:
    b = input('Quer continuar? [S/N]? ').upper().strip()[0]

    if b == 'S':
        x = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
             'nove', 'dez', 'onze', 'doze', 'treze','quatorze', 'quinze',
             'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

        y = int(input('Digite um número entre 0 e 20: '))

        while y not in range(len(x)):
            print('Número inválido, tente novamente!', end='')
            y = int(input(' Digite um número entre 0 e 20: '))
        print('Você digitou o número:', x[y])

    else:
        print('Obrigado volte sempre!')
        break

