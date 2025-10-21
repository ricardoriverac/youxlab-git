listapessoas = []
dicionario = {}
mulheres = []
mediamulheres = []
soma = 0
continuar = 'S'
while continuar == 'S':
     dicionario['nome'] = str(input('NOME:'))
     dicionario['sexo'] = str(input('SEXO:[F/M]')).upper().strip()
     dicionario['idade'] = int(input('IDADE:'))

     listapessoas.append(dicionario) 
     dicionario.copy()
     continuar = str(input('QUER CONTINUAR?[S/N]')).upper().strip()

     while continuar not in 'SN':
        print('ERRO.Digite apenas S e N')
        continuar = str(input('QUER CONTINUAR?[S/N]')).upper().strip()
for d in listapessoas:
    soma = sum(dicionario['idade'])
    numeros = len(dicionario['idade'])
    media = soma / numeros
    media.append(dicionario['idade'])
    if dicionario['sexo'] in 'F':
        mulheres.append(dicionario['nome'])
print(f'A MÉDIA DAS IDADES É:{media}')
print(f'AS MULHERES CADASTRADAS FORAM:{mulheres}')
print(F'AS IDADES ACIMA DA MÉDIA FORAM: {mediamulheres}')
print(f'FORAM CADASTRADAS {len(listapessoas)} PESSOAS')