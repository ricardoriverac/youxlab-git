#dados = {'nome': 'Pedro', 'idade': 25}
#print(dados['nome'])
#print(dados['idade'])



#dados['sexo'] = 'M'        # adiciona nova chave
#del dados['idade']         # apaga uma chave
#print(dados)





#filme = {
  #  'título': 'Star Wars',
 #   'ano': 1977,
 #   'diretor': 'George Lucas'
#}

#print(filme.values())  # mostra apenas os valores
#print(filme.keys())    # mostra apenas as chaves
#print(filme.items())   # mostra chaves e valores

#for k, v in filme.items():
#    print(f'O {k} é {v}')







#filme1 = {'título': 'Star Wars', 'ano': 1977}
#filme2 = {'título': 'Avengers', 'ano': 2012}
#filme3 = {'título': 'Matrix', 'ano': 1999}

#locadora = [filme1, filme2, filme3]
#print(locadora[0]['título'])   # acessa 'Star Wars'
#print(locadora[1]['ano'])      # acessa 2012




#estado = {}
#brasil = []

#for i in range(0, 3):
#    estado['uf'] = input('Unidade Federativa: ')
#    estado['sigla'] = input('Sigla do Estado: ')
#    brasil.append(estado.copy())   # precisa usar copy()

#for e in brasil:
#    for v in e.values():
#        print(v, end=' ')
#    print()