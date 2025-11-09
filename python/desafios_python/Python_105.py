def notas(*numero,sit=False):
    """
    ->função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceitar várias)
    :param sit: valor opcional, indicado se deve ou não adicionar a situção
    :return: dicionário com vários informações sobre a situação da turma.
    """


    resposta = dict()
    resposta['total'] = len(numero)
    resposta['maior'] = max(numero)
    resposta['menor'] = min(numero)
    resposta['media'] = sum(numero)/len(numero)
    if sit:
        if resposta['media'] >= 7:
            resposta['situação'] = 'Boa'
        elif resposta['media'] >= 5:
            resposta['situação'] = 'RAZOÁVEL'
        else:
            resposta['situação'] = 'RUIM'
    return resposta

resposta = notas(5.5,2.5,1.5, sit=True)
print(resposta)