a1 = int(input('Digite o primeiro termo da p.a: '))
r = int(input('Digite a razão dessa p.a: '))
soma = a1
for x in range(1, 11):
    print('O {}º termo é {}'.format(x, soma), end=' => ')
    soma += r
print('Fim')