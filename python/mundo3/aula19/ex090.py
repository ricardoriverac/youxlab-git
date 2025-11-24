# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dicionario = {}
nome = input('Digite seu nome: ')
nota1 = float(input('Digite sua primeira nota tirada na prova: '))
nota2 = float(input('Digite sua segunda nota tirada na prova: '))
medi = (nota1 + nota2) / 2
if medi >=6.0:
   situacao = 'Aprovado!'
else:
   situacao = 'Reprovado.'
dicionario [nome] = {"media": medi, "situação": situacao}
print('----BOLETIM----')
for nome, dados in dicionario.items():
    print(f"Nome: {nome}")
    print(f"A média foi de: {dados['media']}")
    print(f'Você foi {situacao}')
