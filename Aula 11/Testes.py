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
