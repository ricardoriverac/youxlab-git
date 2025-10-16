dadosPrincipal = []
nomes =  [] #0
notas = [] #1
media = [] #2

continuar = 'S'

while continuar == 'S':
    nome = str(input('Digite o nome do Aluno: '))
    notaUm = float(input('Digite a primeira nota: '))
    notaDois = float(input('Digite a segunda nota: '))
    calculoMedia = (notaUm + notaDois) / 2

    dadosPrincipal.append([nome, [notaUm, notaDois], calculoMedia])

    nomes.clear()
    notas.clear()
    media.clear()

    continuar =  str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print(dadosPrincipal)

print('-' * 27)
print(f'Nº {"NOME":^10} {"MÉDIA":^20}')
print('-' * 27)

for i, aluno in enumerate(dadosPrincipal):
    print(f'{i} {dadosPrincipal[i][0]:^10} {dadosPrincipal[i][2]:^21}')

print('-' * 27)

while True:
    notaIndividual = int(input('Qual aluno você deseja ver a nota \033[33mindividual\033[m? (Digite 999 para interromper): '))
    if notaIndividual == 999:
        break
    print(f"Notas de {dadosPrincipal[notaIndividual][0]} são {dadosPrincipal[notaIndividual][1]}")