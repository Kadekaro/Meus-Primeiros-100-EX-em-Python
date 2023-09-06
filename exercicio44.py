valor = float(input('Digite o preço do produto que quer comprar: R$ '))
print('Digite 1 pra ser à vista no dinheiro ou cheque!;\n'
      'Digite 2 pra ser à vista no cartão;\n'
      'Digite 3 pra ser em até 2x no cartão;\n'
      'Digite 4 pra ser em 3x ou mais no cartão.')
pagamento = input('Digite o número correspondente a opção de pagamento que será efetuado: ').strip()
if pagamento == '1':
    print('Essa opção de pagamento te fornece 10% de desconto, '
          'e o valor final de sua compra será de R${:.2f} reais'.format(valor - (valor * 0.1)))
elif pagamento == '2':
    print('Essa opção de pagamento te fornece 5% de desconto, '
          'e o valor final de sua compra será de R${:.2f} reais'.format(valor - (valor * 0.05)))
elif pagamento == '3':
    print('Essa opção de pagamento não tem desconto, '
          'o valor final do produto será de R${:.2f} reais'.format(valor))
elif pagamento == '4':
    print('Essa opção de pagamento acrescenta 20% de juros em sua compra, '
          'e o valor final do produtro será de R${:.2f} reais'.format(valor + (valor * 0.2)))
else:
    print('Digite somente 1, 2, 3 ou 4 para escolher a forma de pagamento!')
