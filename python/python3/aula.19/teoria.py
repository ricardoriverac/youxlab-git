#Dicionários em Python são coleções mutáveis de pares chave-valor, 
# onde cada chave é única e usada para acessar o valor associado. 
# Eles funcionam como um sistema de "rótulos" (chaves) para dados (valores) e são acessados 
# por sua chave, não por um índice numérico como nas listas. 
# Funções como len(), keys(), values(), items(), update(), pop() e get() permitem manipular
#  iterar e gerenciar os dicionários de forma eficiente. 
#len(dicionario): Retorna o número de pares chave-valor no dicionário.
#dicionario.keys(): Retorna uma visualização de todas as chaves do dicionário.
#.values(): Retorna uma visualização de todos os valores do dicionário.
#.items(): Retorna uma visualização de todos os pares chave-valor (tuplas) do dicionário.
#.update(outro_dicionario): Adiciona os pares chave-valor de outro dicionário ao dicionário atual, ou atualiza valores existentes.
#.pop(chave): Remove o item com a chave especificada e retorna o seu valor.
#.popitem(): Remove o último item inserido no dicionário (em Python 3.7+).
#.get(chave, valor_padrao): Retorna o valor da chave especificada. Se a chave não existir, retorna o valor_padrao ou None se nenhum for especificado.
#.setdefault(chave, valor_padrao): Retorna o valor da chave se ela existir; caso contrário, insere a chave com o valor padrão e a retorna.
#del [chave]: Remove um item específico pelo seu nome.
#.clear(): Remove todos os itens do dicionário. 
#dict () cria um novo dicionario assim como o somente usando chaves {}


brasil = []
estado1 = {'uf': 'Rio de janeiro','sigla': 'RJ'}
estado2 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])