def notas(*n, situacao=False):
    
    
    
    
    
    i = dict()
    i['total_notas'] = len(n)
    i['maior_nota'] = max(n)
    i['menor_nota'] = min(n)
    i['media_turma'] = sum(n) / len(n)
    if situacao:
        if i['media'] >= 8:
            i['situacao'] = 'Situação boa!'
        elif i['media'] >= 5:
            i['situacao'] = 'Situação razoavél!'
        else:
            i['situacao'] = 'Situação ruim!'
    return i

usandoFuncao = notas()
print(usandoFuncao)