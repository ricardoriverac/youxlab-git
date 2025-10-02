# vermelho com fundo amarelo em negrito
print('\033[1;31;43mOlá, Mundo!\033[m')

# fundo lilás sublinhado
print('\033[4;30;45mOlá, mundo!\033[m')

# letra amarela fundo azul
print('\033[0;33;44mOlá, Mundo!\033[m')

# duas ou mais variaveis
a=3 
b=5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}')

#mudar a cor de uma variavel
nome = 'Marcela'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome,'\033[m' ))


# Código  Estilo
#0 'None' 
#1 'Bold' 
#4 'Underline'
#7 'Negative'

# cor do texto
#30 - Preto
#31 - Vermelho
#32 - Verde
#33 - Amarelo
#34 - Azul
#35 - Magenta
#36 - Ciano
#37 - Cinza 

# fundo do texto 
#40 - Preto
#41 - Vermelho
#42 - Verde
#43 - Amarelo
#44 - Azul
#45 - Magenta
#46 - Ciano
#47 - Cinza 
