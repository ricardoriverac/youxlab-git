pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 16}
pessoas['peso'] = 98.5 # Adiciona o peso

#pessoas['nome'] = 'Leandro'  Substitui 'João' por 'Leandro'
#del pessoas['sexo'] Apaga a variável sexo do Dicionário

for k, v in pessoas.items():
    print(f'{k} = {v}')