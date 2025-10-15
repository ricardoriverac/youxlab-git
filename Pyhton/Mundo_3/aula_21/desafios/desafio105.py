def nota(* numero, show=False):
    total = 0
    soma = 0
    for c in numero:
        soma = soma + c
        if total == 0 or c > maior:
            maior = c
        if total == 0 or c < menor:
            menor = c
        total = total + 1
    media = soma / total
    resultado = {f'valor total: {total} - maior nota: {maior} - menor nota: {menor} - soma: {media} - media: {media}'}
    if show:
        if media >= 7:
            resultado['situação'] = "BOA"
        elif media >= 5:
            resultado['situação'] = "RAZOÁVEL"
        else:
            resultado['situação'] = "RUIM"
    return resultado


resposta = nota(5.5, 2.5, 6, 6.5, show=True)
print(resposta)