print('-' * 40)
print(f'{"LISTAGEM DE PREÇO" :^40}')   # PRESTAR MUITA ATENÇÃO NA FORMATAÇÃO!
print('-' * 40)
lista = ('caneta', 1, 'caderno', 10, 'amaciante', 13, 'roupa', 40)

#print(f'''{lista[0]}........................R$ {lista[1]:.2f}
#{lista[2]}......................R$ {lista[3]:.2f}
#{lista[4]}....................R$ {lista[5]:.2f}
#{lista[6]}........................R$ {lista[7]:.2f}''')



#metodo do Guanabara abaixo \/


for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'R$ {lista[item]:>.2f}')