'''
Faça um programa que tenha uma função notas() que pode receber várias 
notas de alunos e vai retornar um dicionário com as seguintes informações:

Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação (opcional)
'''

#Resposta

def notas(*n, sit=False):
    dicionario = {}
    dicionario['total'] = len(n)
    dicionario['maior'] = max(n)
    dicionario['menor'] = min(n)
    dicionario['media'] = sum(n) / len(n)
    
    if sit:
        if dicionario['media'] >= 7:
            dicionario['situação'] = 'Boa'
        elif dicionario['media'] >= 5:
            dicionario['situação'] = 'Razoável'
        else:
            dicionario['situação'] = 'Ruim'
    
    return dicionario


# Programa principal
resp = notas(8.5, 9.2, 7.3, 5.5, sit=True)
print(resp)
