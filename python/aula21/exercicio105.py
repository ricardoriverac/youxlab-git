def notas(*n, sit=False):
    boletim = {}
    boletim['total'] = len(n)
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['media'] = sum(n)/len(n)
    if sit:
        if boletim['media'] >= 7:
            boletim['situação'] = 'BOA'
        elif boletim['media'] >= 5:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'RUIM'
    return boletim

resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)        