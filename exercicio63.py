n = int(input('Digite um número: '))
a = 0
b = 0
soma = 0
while soma < n - 2:                    # esse é o método que eu fiz abaixo está o do Guanabara!
    a, b = a + b, a
    soma += 1
    if a == 0:
        print(a, end=' -> ')
        a += 1
        a, b = a + b, a
        print(a, end='')
    print(' -> {}'.format(a), end='')

'''print('=-=' * 30)
print('Sequência de Fibonacci')
print('=-=' * 30)
n = int(input('Digite quantos termos da sequência de Fibonacci você quer ver: '))
t1 = 0
t2 = 1
print('~' * 90)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:                                            #  <<< método que o Guanabara mostra no curso
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> Fim.')
print('~' * 90)'''
