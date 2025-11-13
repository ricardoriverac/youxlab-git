def notas(* numero, situacao=False):
    notasAluno = {}

    notasAluno['total'] = len(numero)
    notasAluno['maiorNota'] = max(numero)
    notasAluno['menorNota'] = min(numero)
    notasAluno['mediaTurma'] = sum (numero) / len(numero)
    notasAluno['situacao'] = 'Aprovado'

    if situacao:
        if notasAluno['mediaTurma'] >= 7:
            notasAluno['situacao'] = 'Aprovado'

        elif notasAluno['mediaTurma'] >= 4.5:
            notasAluno['situacao'] = 'Recuperação'

        elif notasAluno['mediaTurma'] < 4.5:
            notasAluno['situacao'] = 'Reprovado'

    return notasAluno

#Código Principal
respota = notas(5.5, 9.5, 10, 6.5, situacao=True)
print(respota)