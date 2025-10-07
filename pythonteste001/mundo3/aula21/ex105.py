def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :para n: Uma ou mais notas dos alunos (aceita  varias)
    :para sit: valor opcional, indicando se deve ou não adicionar a solução.
    :return: dicionário com várias informações sobre a turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'boa'
        elif r['media'] >= 5:
            r['situacao'] = 'mediana'
        else:
            r['situacao'] = 'ruim'
    return r


resposta = notas(5.5, 2.5, 1.5, sit=True)
print(resposta)
help(notas)