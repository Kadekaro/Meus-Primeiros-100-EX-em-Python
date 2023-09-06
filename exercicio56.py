somador_idades = 0
cont = 0
nome_mais_velho = ''
idade_mais_velho = 0
for i in range(1, 5):
    sexo = input('Digite o sexo: ').upper().strip()
    if sexo == 'MASCULINO':
        y = input('nomes: ').capitalize().strip()
        x = int(input('Digite a idade: '))
        somador_idades += x
        if i == 1:
            nome_mais_velho = y
            idade_mais_velho = x
        elif idade_mais_velho < x:
            nome_mais_velho = y
            idade_mais_velho = x
    else:
        y = input('nomes: ').capitalize().strip()
        x = int(input('Digite a idade: '))
        somador_idades += x
    if x < 20 and sexo == 'FEMININO':
        cont += 1
print('A media de idade desse grupo é de {} anos'.format(int(somador_idades / 4)))
print('{} mulhere(s) tem abaixo de 20 anos!'.format(cont))
print('O nome do homem mais velho é {} e sua idade é {} anos !'.format(nome_mais_velho, idade_mais_velho))
