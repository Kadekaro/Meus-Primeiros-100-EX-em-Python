from datetime import date
dicionario = {}
dicionario['Nome:'] = str(input('Digite seu nome: ')).strip().capitalize()
dicionario['Ano de Nascimento:'] = int(input('Digite seu ano de nascimento(aaaa): '))
dicionario['Idade:'] = date.today().year - dicionario['Ano de Nascimento:']
dicionario['CTPS:'] = int(input('Digite o número dela (0 se não tem): '))
if dicionario['CTPS:'] > 0:
    dicionario['Ano de Contratação'] = int(input('Digite o ano que você foi contratado(a): '))
    dicionario['Salário:'] = float(input('Digite o seu salário: '))
    dicionario['Aposentadoria: '] = (dicionario['Ano de Contratação'] + 35) - dicionario['Ano de Nascimento:']
    del dicionario['Ano de Nascimento:']
    print()
    print('=-' * 50)
    print()
else:
    print()
    print('=-'*50)
    print()
    del dicionario['CTPS:']
    print(f"Sr(a) {dicionario['Nome:']}, você nunca trabalhou registrado!")
    del dicionario['Ano de Nascimento:']
for k, v in dicionario.items():
    print(f'{k} tem o valor de {v}!')
