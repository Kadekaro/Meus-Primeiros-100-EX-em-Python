print('=-=' * 30)
print('{:^85}'.format('\033[4;34mLOJA SUPER BARATÃO\033[m'))
print('=-=' * 30)
total = prod1000 = cont = menor = 0
x = ' '
while True:
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    total += preco
    cont += 1
    if preco >= 1000:
        prod1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        x = produto
    continuar = ' '
    while continuar not in 'NS':
        continuar = input('Quer continuar? [S/N]: ').upper().strip()[0]
    if continuar == 'N':
        break
print('=-=' * 30)
print('{:^94}'.format('\033[4;031mFIM DO PROGRAMA\033[m'))
print(f'Você efetuou uma compra de R$ {total:.2f} reais!')
print(f'{prod1000} produto(s) custam mais de R$ 1000,00 reais!')
print(f'O produto com o menor preço foi a(o) {x} e seu preço é de RS:{menor:.2f} reais!')