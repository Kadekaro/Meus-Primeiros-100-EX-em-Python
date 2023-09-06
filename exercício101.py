print('-'*50)
x = int(input('Digite o ano de nascimento: '))


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    elif idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    elif 16 <= idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: NÃO VOTA!'


print(voto(x))
print('-'*50)
