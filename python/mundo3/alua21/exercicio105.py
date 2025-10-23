def notas(*notas, sit=False):

    total = len(notas)
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / total

    resultado = {
        'total': total,
        'maior': maior,
        'menor': menor,
        'média': media
    }

    if sit:
        if media >= 7:
            resultado['situação'] = 'Boa'
        elif media >= 5:
            resultado['situação'] = 'Razoável'
        else:
            resultado['situação'] = 'Ruim'

    return resultado


 
resp = notas(5.5, 9, 8.5, 10, sit=True)
print(resp)