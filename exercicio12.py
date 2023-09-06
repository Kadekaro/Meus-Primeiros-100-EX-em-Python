produto = float(input('\033[34mDigite o preço de um produto: '))
preço_com_desconto = produto - (produto*0.05)
print('Você irá pagar {}R${:.2f}!{}\033[34m(com o desconto de 5%)!\033[m'.format('\033[4;31m', preço_com_desconto, '\033[m'))

