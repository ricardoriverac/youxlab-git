termo1 = int(input('Digite o primeiro número: '))
razao = int(input('Digite a razão: '))
quantos = int(input('Quatos termos você quer?'))
conta = 1
resultado = 0
mais = quantos
while mais != 0:
    resultado = resultado + mais
    while conta <= resultado:
        print(termo1, '>', end=' ')
        termo1 = termo1 + razao
        conta = conta + 1
    mais = int(input('Quantos termos mais vc deseja? '))
print(f'no total foram {resultado} termos demonstrados')
