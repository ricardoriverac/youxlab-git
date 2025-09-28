mulheres20 = 0
homens = 0
pessoa_18 = 0
condicao = 'sim'
while condicao == 'sim':
    idade = int(input('Qual sua idade?: '))
    sexo = str(input('Qual seu sexo? [Mm/Ff]: ')).upper()
    if idade >=18:
        pessoa_18 +=1
        if sexo == 'M':
            homens +=1
        if sexo == 'F' and idade < 20:
            mulheres20 +=1    
    condicao = str(input('Você quer continuar se cadastrando?: '))
print(f'no total teve {pessoa_18} pessoas com mais de 18 anos, {homens} homens cadastrados e {mulheres20} mulheres com menos de 20 anos')