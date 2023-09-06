num = int(input('\033[36mDigite um número inteiro: '))
x = input('Qual é a base de conversão que você quer seu número? '
          'Escolha entre:\033[m \033[31m"1" para binário, "2" para octal ou "3" para hexadecimal!\033[m\033[36m R:\033[m ').strip()
binario = bin(num).replace('0b', '')
octal = oct(num).replace('0o', '')
hexadecimal = hex(num).replace('0x', '')
if x == '1':
    print('\033[34mO número inteiro\033[m \033[31m{}\033[m \033[34mque você escolheu em binário corresponderá à: '
          '{}{}{}'.format(num, '\033[31m', binario, '\033[m'))
if x == '2':
    print('\033[34mO número inteiro\033[m \033[31m{}\033[m \033[34mque você escolheu em octal corresponderá à: '
          '{}{}{}'.format(num, '\033[31m', octal, '\033[m'))
if x == '3':
    print('\033[34mO número inteiro\033[m \033[31m{}\033[m \033[34mque você escolheu em hexdecimal corresponderá à: '
          '{}{}{}'.format(num, '\033[31m', hexadecimal, '\033[m'))
