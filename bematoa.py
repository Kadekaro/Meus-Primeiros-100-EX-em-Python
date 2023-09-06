'''def str_to_bin(string):
    binario = ''
    for i in string:
        binario += bin(ord(i))[2::] + ' '
    return binario

text = str(input("Entre com um texto: ")) # transformação de decimal para binário
binary = str_to_bin(text)
print(binary)


binary = str(input("Entre com um binario: "))
text = bin_to_str(binary)
print(text)
input()'''

notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0
while x < len(notas):
    notas[x] = float(input('Digite um valor: '))
    soma += notas[x]
    x += 1
x = 0
while x < len(notas):
    print(f'Nota {x+1}: {notas[x]}')
    x += 1
print(f'A média é {soma/x:.2f}')
