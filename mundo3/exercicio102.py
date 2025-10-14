def notas(*ns, sit=False):
    """
    -> Analisa as notas e situação de vários alunos.
    :param ns: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    ns = tuple(valor for valor in ns if bool(valor) != valor)
    print('\n', '-' * 30, sep='')
    dicio = dict()
    dicio['total'] = len(ns)
    dicio['maior'] = max(ns)
    dicio['menor'] = min(ns)
    dicio['média'] = round(sum(ns) / len(ns), 3)
    if sit:
        if dicio['média'] >= 7:
            dicio['situação'] = 'BOA'
        elif dicio['média'] >= 5:
            dicio['situação'] = 'RAZOÁVEL'
        else:
            dicio['situação'] = 'RUIM'
    return dicio
info = notas(5.5, 2.5, 1.5, sit=True)  # notas(3.5, 2, 6.5, 2, 7, 4)
print(info)
help(notas)