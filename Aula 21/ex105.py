def notas(* num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
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
    if sit:
        if media >= 7:
            retorno['situação'] = "BOA"
        elif media >= 5:
            retorno['situação'] = "RAZOÁVEL"
        else:
            retorno['situação'] = "RUIM"
    return retorno


resposta = notas(7.5, 3.5, 10, 8.5, sit=True)
print(resposta)