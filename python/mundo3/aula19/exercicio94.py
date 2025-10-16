pessoas=[]
pessoa={}
listaMulheres=[]
listaIdadeAcimaMedia=[]
somaIdades=0
contadorPessoas=0

resposta='S'
while resposta != 'N':
    pessoa['nome']=str(input("Qual o nome? "))
    pessoa['sexo']=str(input("Sexo M/F? ")).upper()
    pessoa['idade']=int(input("Qual a idade? "))
    pessoas.append(pessoa.copy())
    
    somaIdades= somaIdades + pessoa['idade']
    contadorPessoas += 1
    
    resposta=str(input('QUer continuar? S/N ')).upper()
    
mediaIdade=somaIdades/contadorPessoas
    

    
for p in pessoas:
    if p ['sexo'] == 'F'.upper():
        listaMulheres.append(p)
    if contadorPessoas > mediaIdade:
        listaIdadeAcimaMedia.append(contadorPessoas)


print(f'Foram cadastradas {contadorPessoas} pessoas')
print(f'As mulheres cadastradas foram {listaMulheres}')
print(f'A media de idade é {mediaIdade}')
print(f'As pessoas cadrastadas que tem idade acima da media é {listaIdadeAcimaMedia}')