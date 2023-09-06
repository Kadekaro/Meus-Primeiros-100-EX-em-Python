print('=-=' * 30)
print('                              {CADASTRO DE PESSOAS}')
print('=-=' * 30)
maior_de_18 = masculinos = mulheres_menor = 0
while True:
    s = ' '
    idade = int(input('Digite sua idade: '))
    while s not in 'MF':
        s = str(input('Digite seu sexo: ')).strip().upper()[0]
    if idade >= 18:
        maior_de_18 += 1
    if s == 'M':
        masculinos += 1
    if s == 'F' and idade <= 20:
        mulheres_menor += 1
    x = ' '
    while x not in 'SN':
        x = input('Quer cadastrar mais uma pessoa? [S para SIM / N para NÃO]: ').upper().strip()[0]
        print('=-=' * 30)
    if x == 'N':
        break
print('=-=' * 30)
print('                             << FIM DO PROGRAMA >>')
print('=-=' * 30)
print(f'{maior_de_18} pessoa(s) é(são) maior(es) de 18 anos')
print(f'{masculinos} é(são) do sexo masculino')
print(f'{mulheres_menor} é(são) do sexo feminino abaixo dos 20 anos')



