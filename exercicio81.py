lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    pergunta = input('Quer continuar? (S/N)! R: ').strip().upper()[0]
    if pergunta == 'N':
        print('=-' * 30)
        break

print(f'Há {len(lista)} números digitados na lista!')
lista.sort(reverse=True)
print(f'Os números em forma decrescente são: {lista}')
pos = 0
if 5 in lista:
    print('O valor 5 está na lista!')
    print('Nas posições', end='')
    for pos, v in enumerate(lista):
        if v == 5 in lista:
            print(f'...{pos + 1}', end='')
else:
    print('O valor 5 não foi encontrado na lista!')











