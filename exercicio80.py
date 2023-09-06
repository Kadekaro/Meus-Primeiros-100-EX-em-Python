
# colocando valores em ordem sem usar o método "sort"

lista = list()
for x in range(0, 5):
    y = int(input('Digite um número: '))
    if x == 0 or y > lista[-1]:   # << se é o primeiro valor add ele na lista ou se o valor for maior que o
        lista.append(y)                          # ultimo valor add ele tb.
    else:
        pos = 0
        while pos < len(lista):         # << percorre a lista toda do 0 ate o ultimo elemento que é o 4
            if y <= lista[pos]:         # aotodo (5 numeros
                lista.insert(pos, y)    # << verifica se y é menor ou igual a todos elementos ja colocados na lista
                break                   # se ele for, ele insere no meio esse valor na posição correta
            pos += 1


print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')




