'''pessoas = {'nome': 'Marcela', 'sexo':'F','idade':16}
print(pessoas)
print(pessoas['nome']) #pra mostrar o nome
print(pessoas['idade']) #pra mostrar idade
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.') #A marcela tem 16 anos #referenciar elementos [] 
#declarar {}
print(pessoas.keys()) #para mostrar nome, sexo e idade.
print(pessoas.values()) #para mostrar valores
print(pessoas.items())#mostra os itens
'''

#de outra forma
'''for k in pessoas.keys():
    print(k)'''
'''for k in pessoas.values():
    print(k)'''
'''for k in pessoas.items():
    print(k)'''
'''for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''del pessoas ['sexo'] #apagar o elemento sexo 
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''pessoas['nome']= 'ana julia' #modificar nome
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''pessoas['peso'] = 54.0  #adicionar o peso
for k, v in pessoas.items():
    print(f'{k} = {v}')'''


'''brasil = []
estado1 = {'uf': 'Minas Gerais','sigla':'MG'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil) #mostra tudo
print(brasil[0]) #mostra o estado 1
print(brasil[1])#mostra o estado 2
print(brasil[0]['uf']) #mostra minas gerais '''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla']= str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    for e in brasil:
        for v in e.values():
            print(v)






'''for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')'''
