from datetime import datetime
anoAtual = datetime.now().year
maioridadeCount = 0
menorIdadeCount = 0
for c in range(7):
    anoNascimento = int(input(f'Digite o ano de nascimento da {c+1}ª pessoa: '))
    idade = anoAtual - anoNascimento
    if idade >= 18:
        maioridadeCount += 1
    else:
        menorIdadeCount += 1
print(f'\nTotal de pessoas com maioridade: {maioridadeCount}')
print(f'Total de pessoas sem maioridade: {menorIdadeCount}')
