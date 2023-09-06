from datetime import date
x = []
y = []
for c in range(1, 8):
    i = int(input('Digite a data de nascimento de 7 pessoas: '))
    b = date.today().year - i
    if b < 21:
        x.append(b)
    else:
        y.append(b)
print('{} pessoa(s) são(é) de menores!'.format(len(x)), end=' ')
print('{} pessoa(s) são(é) de maiores!'.format(len(y)))

# no video de resolução ele usa 2 contadores 1 pra maior outro pra menor
# os contadores substituiriam as 2 listas (x, y)