def notas(* num, show=False):
    total = 0
    soma = 0
    for c in num:
        soma += c
        if total == 0 or c > maior:
            maior = c
        if total == 0 or c < menor:
            menor = c
        total += 1
    media = soma / total
    retorno = {'total': f'{total}', 'maior': f'{maior}', 'menor': f'{menor}', 'soma': f'{media}', 'media': f'{media}'}
    if show:
        if media >= 7:
            retorno['situação'] = "BOA"
        elif media >= 5:
            retorno['situação'] = "RAZOÁVEL"
        else:
            retorno['situação'] = "RUIM"
    return retorno


resp = notas(5.5, 2.5, 6, 6.5, show=True)
print(resp)