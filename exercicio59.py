'''a = float(input('\033[34mDigite um valor: '))
b = float(input('Digite outro valor: '))
print('\033[1;32mMENU:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair\033[m')
x = input('\033[34mDigite sua opção aqui(1 a 5): \033[m')
if x == '5':
    print('\033[31mMuito obrigado volte sempre!')
else:
    while x != 5:
        if x == '1':
            print('A soma entre {} e {} será de {}!'.format(a, b, a + b))
            break
        elif x == '2':
            print('A multiplicação entre {} e {} será de {}!'.format(a, b, a * b))        # Esse programa eu que fiz mas ele não retorna o menu novamente para escolher outra opção!
            break
        elif x == '3' and a > b:
            print('O maior entre eles é o número {}!'.format(a))
            break
        elif x == '3' and b > a:
            print('O maior valor é o número {}!'.format(b))
            break
        elif x == '4':
            print('\033[31mDigite novos números abaixo!')
            a = float(input('\033[34mDigite um valor: '))
            b = float(input('Digite outro valor: \033[m'))
            print('\033[1;32mMENU:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair\033[m')
            x = input('\033[34mDigite sua opção aqui(1 a 5): \033[m')
            if x == '5':
                print('\033[31mMuito obrigado volte sempre!')'''

# Abaixo eu vou criar um programa que retorna o menu novamente:

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
opções = 0
while opções != 5:
    print('''
    [1] soma
    [2]produto
    [3]maior
    [4]Digite outros valores
    [5]Sair\n''')
    opções = int(input('Digite a opção que quer realizar de 0 a 5: '))
    if opções == 1:
        print('A soma entre {} e  {} é {}!'.format(a, b, a + b))
    elif opções == 2:
        print('O produto entre {} e {} é {}!'.format(a, b, a * b))
    elif opções == 3:
        if a > b:
            print('O maior número entre {} e {} é o número {}!'.format(a, b, a))
        else:
            print('O maior número entre {} e {} é o número {}!'.format(a, b, b))
    elif opções == 4:
        a = float(input('Digite outro primeiro número: '))
        b = float(input('Digite outro segundo número: '))
    elif opções == 5:
        print('Programa terminado! Muito obg! Volte sempre!')
    else:
        print('Opção inválida! Tente novamente!')
    print('=-=' * 20)
