primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('De quanto em quanto está indo: '))
termoAtual = primeiroTermo
contar = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contar <= total:
        print(f'{termoAtual} -> ', end='')
        termoAtual = termoAtual + razao 
        contar += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')