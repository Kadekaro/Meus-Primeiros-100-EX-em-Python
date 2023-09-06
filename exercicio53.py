frase = input('Digite uma frase: ').strip().upper().replace(' ', '')
if frase == frase[::-1]:
    print('Essa frase é palíndrome')
else:
    print('Essa frase não é palíndrome')
