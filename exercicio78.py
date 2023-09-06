lista = []

for elemento in range(1, 6):
    lista.append(int(input(f'Digite um número para a posição {elemento}: ')))

print(f'O maior valor foi o {max(lista)}, e ele está na(s) posição(ões)...', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i + 1}...', end='')

print()

print(f'O menor valor foi o {min(lista)}, e ele está na(s) posição(ões)...', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i + 1}...', end='')
print()

# Abaixo fica o jeito de fazer sem a função embutida max e min do python;
# esse método seria inserido depois do primeiro (for):

maior = 0
menor = 0

'''if elemento == 0:
    maior = menor = lista[elemento]
else:
    if lista[elemento] > maior:
        maior = lista[elemento]
    if lista[elemento] < menor:
        menor = lista[elemento]'''

