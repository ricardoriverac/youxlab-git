pessoas={'nome': 'Gustavo', 'sexo': 'M', 'idade': '12'}
pessoas['nome']='Leandro'
pessoas['peso']=70.8
for k in pessoas.items():
    print(k)
Brasil=[]
estado1={'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2= {'uf': 'São Paulo', 'Sigla': 'SP'}
Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil)
print(Brasil[0]['uf'])
estado=dict()
Brasil=list()
for c in range (0,3):
    estado['uf']=str(input('Unidade federativa:'))
    estado['Sigla']=str(input('Qual a sigla do estado?: '))
    Brasil.append(estado.copy())
print(Brasil)
for e in Brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')