def notas(*num, sit=False):
    """
    Programa para analizar notas de alunos.
    :param num: recebe valor da nota pode ser vários valores
    :param sit: (opcional) se True exibe a situação: Aprovado, Reprovado, recuperação.
    :return: retorna dicionário
    """
    lista = {}
    lista['total'] = len(num)
    lista['maior'] = max(num)
    lista['menor'] = min(num)
    lista['media'] = sum(num) / len(num)
    if sit == True:
        if lista['media'] >= 7:
            lista['sit'] = 'Aprovado'
        elif 5 <= lista['media'] < 7:
            lista['sit'] = 'Recuperação'
        else:
            lista['sit'] = 'Reprovado'
    return lista



resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)

meiabomba = notas(3, 4, sit=True)              #trollname
print(meiabomba)

meiabomba2 = notas(5, 6, sit=True)              #trollname
print(meiabomba2)
print()
help(notas)    