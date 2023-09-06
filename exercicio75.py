n = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
     int(input('Digite outro número: ')), int(input('Digite o último número: ')))
print(f'O valor 9 apareceu {n.count(9)} vez(es).')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3) + 1}º posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
print(f'O(s) valor(es) que é(são) par(es): ', end='')
for t in n:
    if t % 2 == 0:
        print(t, end=' ')
if t % 2 != 0:
    print('Nenhum valor digitado é par!')
