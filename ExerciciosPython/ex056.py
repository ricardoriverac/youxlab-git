somaIdades = 0
nomeHomemVelho = ''
idadeHomemVelho = 0
contadorMulheres20Anos = 0
for c in range(1, 5):
    nome = str(input("Digite o nome da pessoa: "))
    idade = int(input('Digite o idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper()
    somaIdades = idade + somaIdades
    if sexo == 'M':
        if idade > idadeHomemVelho:
            idadeHomemVelho = idade 
            nomeHomemVelho = nome 
    else:
        if idade < 20:
            contadorMulheres20Anos +=1
media = somaIdades / 4
print(f'A idade média do grupo é {media};\nO homem mais velho se chama {nomeHomemVelho};\n{contadorMulheres20Anos} mulheres tem menos de 20 anos.')