print('-'*40)
print('     ANALISANDO E GERANDO DICIONÁRIOS:')
def notas(*n, sit=False): # O QUE A FUNÇÃO 'NOTAS()' FAZ?
                        #Saber quantas notas foram dadas.
                        #Saber qual foi a maior nota.
                        #Saber qual foi a menor.
                        #Calcular a média dessas notas.
                        #E opcionalmente (se quiser), ver se a turma está com a situação BOA, RAZOÁVEL ou RUIM, baseado na média.
    """
    -> Função para analisar notas e situações de vários alunos.
    :parâmetro n: uma ou mais notas dos alunos (aceita várias)
    :parâmetro sit: valor opcional indicando se deve ou não adicionar a situação do aluno
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = {}
    r['total'] = len(n) 
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:                             
        if r['media'] >= 7:
            r['situacao'] = 'BOA!'
        elif r ['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL!'   
        else:
            r['situacao'] = 'RUIM!'
    return r

#PROGRAMA PRINCIPAL
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
#MANUAL: help(notas)