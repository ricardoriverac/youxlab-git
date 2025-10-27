#Repetições utilizando os dicionários

# aula_002.py
# Assunto: Estrutura de repetição com dicionários (for k, v in Dados.items())

# Criamos um dicionário com alguns dados
Dados = {'Nome': 'Juam', 'Idade': 16, 'Sexo': 'Masculino'}

# ==========================
# 2️⃣ Estrutura de repetição "for"
# ==========================
# O método .items() retorna os pares de chave e valor do dicionário.
# Exemplo: [('Nome', 'Juam'), ('Idade', 16), ('Sexo', 'Masculino')]
#
# A estrutura "for k, v in Dados.items()" percorre cada um desses pares.
# Em cada repetição, "k" recebe a chave e "v" recebe o valor.
# Assim, podemos acessar e exibir cada informação separadamente.

for k, v in Dados.items():
    # Aqui, exibimos a chave e o valor de forma organizada.
    print(f'{k}: {v}')



# Saída esperada:
# Nome: Juam
# Idade: 16
# Sexo: Masculino


# aula_002.py
# Assunto: Entendendo por que 'k' mostra apenas as chaves e 'v' apenas os valores no dicionário

# Criamos um dicionário com três pares de dados
Dados = {'Nome': 'Juam', 'Idade': 16, 'Sexo': 'Masculino'}

# =====================================================
# 1️⃣ O que o método .items() faz
# =====================================================
# Quando usamos Dados.items(), o Python retorna um objeto que contém
# todos os pares (chave, valor) do dicionário.
#
# Se imprimirmos isso diretamente, veremos algo assim:
print('Conteúdo de Dados.items():')
print(Dados.items())
print()  # Linha em branco para separar visualmente a saída

# =====================================================
# 2️⃣ Entendendo o resultado de Dados.items()
# =====================================================
# Internamente, o que .items() faz é transformar o dicionário em uma lista de tuplas,
# onde cada tupla contém dois elementos: a chave e o valor.
#
# Exemplo: [('Nome', 'Juam'), ('Idade', 16), ('Sexo', 'Masculino')]

# =====================================================
# 3️⃣ Como o 'for' entende isso
# =====================================================
# Quando fazemos "for k, v in Dados.items()", o Python entende que cada item
# é uma tupla (ex: ('Nome', 'Juam')) e "desempacota" essa tupla automaticamente:
#  - O primeiro elemento vai para a variável k (chave)
#  - O segundo elemento vai para a variável v (valor)

print('Mostrando o loop com desempacotamento:')
for k, v in Dados.items():
    print(f'Chave (k): {k}  -->  Valor (v): {v}')
print()

# =====================================================
# 4️⃣ O que acontece se não desempacotarmos
# =====================================================
# Podemos fazer um teste sem o desempacotamento automático:
print('Mostrando o loop sem desempacotamento:')
for item in Dados.items():
    print(f'Item completo (tupla): {item}')
print()

# Agora, se quisermos acessar manualmente a chave e o valor,
# podemos fazer isso usando índices:
print('Acessando manualmente cada parte da tupla:')
for item in Dados.items():
    print(f'Chave: {item[0]}  -->  Valor: {item[1]}')
print()

# =====================================================
# 5️⃣ Conclusão
# =====================================================
# - .items() transforma o dicionário em pares (chave, valor)
# - for k, v in ... separa automaticamente cada par
# - Por isso, 'k' mostra apenas as chaves e 'v' apenas os valores


