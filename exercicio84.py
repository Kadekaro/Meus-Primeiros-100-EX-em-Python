pessoas = []
lista = []
leve = pesado = 0
while True:
    pessoas.append(str(input('Digite o nome: ')))
    pessoas.append(float(input('Digite o peso: ')))
    if len(lista) == 0:
        leve = pesado = pessoas[1]
    else:
        if pessoas[1] > pesado:       # prestar atenção nessa verificação
            pesado = pessoas[1]
        if pessoas[1] < leve:
            leve = pessoas[1]
    lista.append(pessoas[:])
    pessoas.clear()
    y = str(input('Quer continuar,[S/N]? R: ')).strip().upper()[0]
    if y == 'N':
        break
print('=-'*30)
print(f'Foram cadastrado(s) {len(lista)} pessoa(s)')
print(f'O maior peso foi de {pesado} KG, peso da(o)', end='')
for p in lista:
    if p[1] == pesado:
        print(f'...[{p[0]}]', end='')
print()
print(f'O menor peso foi de {leve} KG', end='')
for p in lista:
    if p[1] == leve:
        print(f'...[{p[0]}]', end='')
print()

