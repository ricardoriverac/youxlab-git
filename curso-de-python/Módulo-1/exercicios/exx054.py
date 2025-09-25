maiores = 0
menores = 0
anoAtual = 2025
for c in range(1, 8):
    anoNascimento = int(input('Digite o ano em que você nasceu: '))
    if anoAtual - anoNascimento < 21:
        menores += 1
    else:
        maiores += 1

print(f'{menores} pessoas ainda são menores de idade, e {maiores} são maiores de idade.')