from time import sleep
casa = float(input('Digite o valor da casa que irá comprar: R$ '))
salario = float(input('Digite qual é o seu salário líquido: R$ '))
anos = float(input('Em quantos anos pretende pagar a casa? R: '))
parcela = casa / (anos * 12)
print('\033[1;31mPROCESSANDO...\033[m')
sleep(3)
if parcela < 0.3 * salario:
    print('\033[36mParabéns, sua proposta foi aprovada e sua prestação será '
          'de{} R${:.2f}{}\033[36m centavos!'.format('\033[1;33m', parcela, '\033[m'))

else:
    print('\033[30;41mDesculpe sua proposta não foi aprovada pois excede 30% do seu salário líquido!\033[m')
