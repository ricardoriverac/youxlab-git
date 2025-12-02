#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
#Quantidade de notas
#A maior nota
#A menor nota
#A média da turma
#A situação (opcional)

def notas(n, situacao=False):
    dados={}
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n) / len(n)
    if situacao:
        if dados['media'] >= 6:
            dados['situacao'] = 'Aprovado'
        else:
            dados['situacao'] = 'Reprovado'
    return dados
conti = 'S'
notas_lista = []
while conti == 'S':
    nota = float(input('Digite a nota: '))
    notas_lista.append(nota)
    conti = input('Você deseja cadastrar mais notas de outros alunos:[S/N]').upper()
resultado = notas(notas_lista, situacao=True)
print(resultado)
