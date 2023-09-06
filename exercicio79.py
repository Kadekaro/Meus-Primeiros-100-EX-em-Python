lista = []
while True:
    x = float(input('Digite quantos valores quiser: '))
    if x not in lista:
        lista.append(x)
        print('Valor add com sucesso...')
    else:
        print('Valor duplicado não vou adicionar a lista!')
    y = input('Deseja continuar? (S/N): ').strip().upper()[0]
    if y == 'N':
        print('=-' * 30)
        break
print(sorted(lista))
