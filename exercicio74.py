from random import randint
x = (randint(1, 11), randint(1, 11), randint(1, 11), randint(1, 11), randint(1, 11))
y = sorted(x)
print(x)
#print(f'O maior dos números aleatórios gerados é: {max(x)}')
#print(f'O menor dos números aleatórios gerados é: {min(x)}')


print(f'O maior dos números aleatórios gerados é: {y[-1]}')
print(f'O menor dos números aleatórios gerados é: {y[0]}')

# 2° formas acima de fazer esse exercício /\