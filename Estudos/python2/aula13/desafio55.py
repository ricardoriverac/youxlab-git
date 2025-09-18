pessoas = int(input('Quantas pessoas serão analisadas? '))
pessoasAvaliadas=0
pesos = 0
pesoMaior= 0
pesoMenor= 1000
for c in range (1, pessoas+1):
    pessoasAvaliadas = pessoasAvaliadas+1
    pesos= float(input(f'Qual o peso da pessoa {pessoasAvaliadas}'))
    

    if pesos > pesoMaior:
        pesoMaior=pesos
    if pesos < pesoMenor:
        pesoMenor=pesos
print(f'O maior peso lido é {pesoMaior}')
print(f'O menor peso lido é {pesoMenor}')