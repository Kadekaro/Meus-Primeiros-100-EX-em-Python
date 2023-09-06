x = input('Digite uma expressão: ')
pilha = []
for simb in x:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            print(pilha)
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) % 2 == 0:
    print('Está é uma expressão válida.')
else:
    print('Está expressão está errada.')
