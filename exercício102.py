def fatorial(n, show=False):
    """
    -> Função fatorial: Calcula o fatorial de um número.
    :param n: número que irá calcular o fatorial.
    :param show: (Parâmetro opcional) escolhe se irá ou não retornar a função fatorial.
    :return: retorna o valor do Fatorial de n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
    if show == True:
        for repetir in range(n, 0, -1):
            print(f'{repetir}', end=' ')
            if repetir > 1:
                print(f'x', end=' ')
        return f'= {f}'
    else:
        print(f'Você optou por não ver o fatorial do número escolhido!')
        return f'O resultado é = {f}'


print(fatorial(5, False))
help(fatorial)