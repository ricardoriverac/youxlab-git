
somaIdades = 0
mediaidade = 0 
nomehomem = 0
idadehomem = 0
mulhereidade = 0
mulhernome = 0
somapessoas = 0
somapessoas2 = 0 
for dados in range (0, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexualidade = input('Por favor, insira o seu sexo(M para masculino e F para feminino): ').upper()
    somaIdades = somaIdades + idade
    mediaidade = idade /4
    if sexualidade == 'M':
        if idade > idadehomem:
            idadehomem = idade
            nomehomem = nome 
            somapessoas += 1
        elif sexualidade == 'F':
            if idade < 20:
                mulhernome = nome 
                mulhereidade = idade
                somapessoas2 += 1
    else:
        print('Erro, por favor tente novamente')
        
print('-------Analizando-------')
print(f'{nome}')
print(f'{idade}')
print(f'{sexualidade}') 
print(f'A media do grupo foi de {mediaidade}')
if somapessoas >= 1:
    print(f'O homem mais velho é {nomehomem} com {idadehomem} anos')
elif somapessoas2 >= 2:
    print(f'As mulheres com menos de 20 anos sao {mulhernome} com {mulhereidade} anos')
    
