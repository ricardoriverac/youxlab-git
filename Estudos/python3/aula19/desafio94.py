pessoas= []
mulheres= []
soma=0
continuacao= 'S'
while continuacao != 'N':
    nome= str(input('Digite seu nome: '))
    sexo= str(input('Digite seu sexo [M/F]').upper())
    while sexo not in ('M', 'F'):
        print(f'Digite novamente seu sexo!')
        sexo=str(input('Digite seu sexo [M/F]').upper())
    if sexo == 'F':
        mulheres.append(nome)
    idade= int(input('Digite sua idade: '))
    soma+=idade
    pessoa= {'NOME': nome, 'SEXO': sexo, 'IDADE': idade }
    pessoas.append(pessoa)
    continuacao= str(input('Você deseja continuar [S/N]').upper())
print(f'A quantidade de pessoas cadastradas foram {len(pessoas)}')
media= soma / len(pessoas)
print(f'A media de idade é {media}')
print(f'As mulheres cadastradas são {mulheres}')
for p in pessoas:
    if p['IDADE'] > media:
            print(f"""As pessoas com idade acima da média são:
                  {p['NOME']}, sexo correspondente à {p['SEXO']} e idade correspondente à {p['IDADE']}""")
    