'''print('=-=' * 20)
print('{:^60}'.format('BANCO CEV'))
print('=-=' * 20)
saque = int(input('Quanto você quer sacar? R: R$'))
sobra = cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0
a = saque % 50
b = a % 20
c = b % 10
d = c % 1
x = True
while x:
    if saque % 50 != 0:
        cedulas50 = saque // 50
        sobra = a
    else:
        cedulas50 = saque // 50
        x = False
    if b != 0:
        cedulas20 = a // 20         # <<  ESSA É MINHA SOLUÇÃO, EU QUE FIZ ASSSIM!
        sobra = b
    else:
        cedulas20 = a // 20
        x = False
    if c != 0:
        cedulas10 = b // 10
        sobra = c
    else:
        cedulas10 = b // 10
        x = False
    if d != 0:
        cedulas1 = c // 1
    else:
        cedulas1 = c // 1
        x = False
print(f'Você irá sacar {cedulas50} nota(s) de 50', end=', ')
print(f'{cedulas20} nota(s) de 20', end=', ')
print(f'{cedulas10} nota(s) de 10', end=', ')
print(f'e {cedulas1} nota(s) de 1!')
print('=-=' * 20)'''

# ABAIXO VOCÊ VERÁ A RESOLUÇÃO DO GUANABARA DO CURSO EM VIDEO \/

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Digite o valor que quer sacar: '))
total = valor
ced = 50
contced = 0
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced > 0:
            print(f'Total de {contced} cédulas de R${ced} reais')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contced = 0
        if total == 0:
            break
print('=' * 30)
print('Muito obrigado! Volte sempre! BANCO CEV!')