# Curso Python #11 - Cores no Terminal
# ANSI - espace sequence - são códigos especiais usados em terminais de texto para controlar a formatação, a cor do texto, o estilo da fonte e a posição do cursor.
# \033[<style(estilo da fonte); text(cor do texto); back(cor do fundo)>m- representar uma cor em python 
#  EXEMPLO
# \033[0;33;44m

# CÓDIGOS PARA ESTILOS - STYLE
# 0 - sem estilo nenhum - none
# 1 - em negrito - bold
# 4 - sublinhado - underline
# 7 - inverte as configurações <o que está no fundo passa para letra e o que esta nas letras passa para o fundo> - negative

# TEXTOS - TEXT
# 30 - branco ->  cinza
# 31 - vermelho
# 32 - verde
# 33 - amarelo
# 34 - azul
# 35 - roxo
# 36 - azul claro
# 37 - cinza -> branco

# CORES DE FUNDO - BACK
# 40 - branco
# 41 - vermelho
# 42 - verde
# 43 - amarelo
# 44 - azul
# 45 - roxo
# 46 - azul claro
# 47 - cinza
 
# EXCESSÃO
# \033[m - preto
# \033[7;30m - branco - 7 = inverte 

# PRÁTICA 
# ex.1
# print('\033[37m Olá pessoa\033[m')
# esse \033[m no final delimita ate aonde essa cor de fundo vai ir 

# ex.2
# a = 3
# b = 8
# print(f'Os valores são \033[31m{a} e \033[31m{b}\033[m')

# ex.3
nome = 'Júlia'
cores = {'limpa': '\033[m',
          'roxo':'\033[35m',
            'vermelho': '\033[31m',
              'pretoebranco': '\033[7,30'}
print(f'Muito prazer em te conhecer, \033[1;35m{nome}\033[m!!!!')
# 
# #











