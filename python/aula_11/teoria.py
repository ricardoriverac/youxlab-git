# cor do texto (vermelho)
print('\033[0;31mOlá, mundo!')

# vermelho com fundo amarelo 
print('\033[0;31;43mOlá, mundo!')

# vermelho com fundo amarelo em negrito 
print('\033[1;31;43mOlá, mundo!')

# diminuir o espaço da cor de fundo - não foi
print('\033[1;31;43mOlá, mundo!\033[m') 

# # Código  Estilo
# 0 'None' 
# 1 'Bold' 
# 4 'Underline'
# 7 'Negative'

# # cor do texto
# 30 - Preto
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelo
# 34 - Azul
# 35 - Magenta
# 36 - Ciano
# 37 - Cinza 

# # fundo do texto 
# 40 - Preto
# 41 - Vermelho
# 42 - Verde
# 43 - Amarelo
# 44 - Azul
# 45 - Magenta
# 46 - Ciano
# 47 - Cinza 

# duas ou mais variaveis 
a = 3
b = 5 
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
 
#  mudar a cor de uma variavel 
nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome,'\033[m' ))
