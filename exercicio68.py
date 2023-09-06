from random import randint
v = 0
while True:
    print('=-=' * 30)
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você escolhe PAR ou ÍMPAR? [P/I] : ')).upper().strip()[0]
        print('=-=' * 30)
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            print(f'Você jogou {jogador} o computador jogou {computador}, e a soma entre eles {total} deu PAR.')
            v += 1
        else:
            print('VOCÊ PERDEU OTÁRIO!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('VOCÊ VENCEU!')
            print(f'Você jogou {jogador} o computador jogou {computador}, e a soma entre eles {total} deu ÍMPAR.')
            v += 1
        else:
            print('VOCÊ PERDEU OTÁRIO!')
            break
    print('Vamos jogar novamente!')
print(f'GAME OVER! Você tentou e venceu {v} vez(es)')
