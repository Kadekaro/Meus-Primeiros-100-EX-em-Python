def escreva(txt):
    print('~'*(len(txt)+5))
    print(f'  {txt}')
    print('~' * (len(txt) + 5))
escreva(input('Digite o texto: ').capitalize())
