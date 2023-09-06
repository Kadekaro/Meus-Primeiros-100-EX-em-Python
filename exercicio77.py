palavras = ('aprender', 'programas', 'linguagens', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'mercado',
            'trabalhador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos.......', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end=' ')