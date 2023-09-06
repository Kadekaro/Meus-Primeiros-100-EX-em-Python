def notas(*i, sit=False):
    """
    Função que retorna um dicionário com o Total, Maior, Menor, Média, Situação(opcional)!
    :param i: recebe todas notas que definirem
    :param sit: Parâmetro opcional que retorna a situação do aluno!
    :return: retorna um dicionário com a situação da nota do aluno!

    Feito pelo excelentíssimo senhor Wesley!
    """
    print('-' * 50)
    cont = s = menor = maior = 0
    n = {}
    for k, v in enumerate(i):
        cont += 1
        n["Total"] = cont
        s += v
        if k == 0:
            menor = maior = v
        else:
            if k > 0:
                if v > maior:
                    maior = v
                if v < menor:
                    menor = v
    n["maior"] = maior
    n["menor"] = menor
    n["media"] = s / len(i)
    if sit:
        if n["media"] >= 7:
            n["Situação"] = "Boa"
        elif 5 <= n["media"] < 7:
            n["Situação"] = "Razoável"
        else:
            n["Situação"] = "Ruim"
    return n


# programa principal:
resp = notas(1, 6, 7, 5, sit=True)
print(resp)
print('-'*50)
print()
help(notas)


