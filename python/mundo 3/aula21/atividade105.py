def notas(*n,sit=False):
    boletim = dict()
    boletim["total"] = len(n)
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['média'] = sum(n) / len(n)

    if sit:
        if boletim['média'] >= 7:
            boletim['situação'] = 'BOA'
        elif boletim['média'] >= 5:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'RUIM'

    return boletim
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)