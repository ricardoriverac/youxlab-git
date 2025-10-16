# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias
# notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)

def notas(*notas): # * -> recebe quantos argurmentos quiser, tratar esses argumentos depois como tupla
    notasdic={
        'qtd_notas': len(notas),
        'maior_nota': 0, 
        'menor_nota': 10,
        'media_nota': 0,
        'situacao': None
    }
    soma = 0
    for n in notas:
        soma += n
        if n > notasdic['maior_nota']:
            notasdic['maior_nota'] = n
        if n < notasdic['menor_nota']:
            notasdic['menor_nota']=n
        
    notasdic['media_nota']=soma/len(notas)
    if notasdic['media_nota'] >= 7:
        notasdic['situacao']='APROVADO'
    else:
        notasdic['situacao']='REPROVADO'

    return notasdic




j = notas(3, 8, 9, 2, 7, 1, 4, 6)
k = notas(1)

print(j)
print(k)





