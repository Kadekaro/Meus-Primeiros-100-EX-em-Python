cont = 0
print('=-=' * 30)
n = int(input('Você quer ver a tabuada de qual valor? '))
print('=-=' * 30)
while cont != 11:
    print(f"{cont:2} x {n} = {cont * n}")
    cont += 1
    if cont == 11:
        cont = 0
        print('=-=' * 30)
        n = int(input('Você quer ver a tabuada de qual valor? '))
        print('=-=' * 30)
        if n < 0:
            print('Programa de tabuada encerrado. Volte sempre!')
            break

