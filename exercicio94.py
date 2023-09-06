pessoas = list()
dados = {}
mulheres = []
soma = 0
while True:
    dados['Nome'] = str(input('Nome: ')).capitalize()
    dados['Sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
    dados['Idade'] = int(input('Idade: '))
    if dados['Sexo'] == 'F':
        mulheres.append(dados['Nome'])
    soma += dados['Idade']
    pessoas.append(dados.copy())
    dados.clear()
    x = str(input('Quer continuar?[S/N]? ')).strip().upper()[0]
    if x == 'N':
        break
print('=-' * 50)
media = soma / len(pessoas)
print(f'-Foram cadastradas {len(pessoas)} pessoas')
print(f'-A media da idade do grupo foi {media:.2f} anos')
print(f'-As mulheres são {mulheres}')
print(f'-Lista de pessoas que estão acima da média: ')
for x in pessoas:
    if x['Idade'] > media:
        print(f'   *{x}')