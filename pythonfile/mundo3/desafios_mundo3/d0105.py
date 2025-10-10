def notas(*numero, sit=False):
    
    
    total = len(numero)
    maior = numero[0]
    menor = numero[0]
    soma = 0

    
    for nota in numero:
        soma += nota
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota

    media = soma / total

    
    resultado = {
        'total': total,
        'maior': maior,
        'menor': menor,
        'média': media
    }

    if sit:
        if media >= 7:
            resultado['situação'] = 'BOA'
        elif media >= 5:
            resultado['situação'] = 'RAZOÁVEL'
        else:
            resultado['situação'] = 'RUIM'

    return resultado



resp = notas(6, 7.5, 9, 3.5, sit=True)
print(resp)