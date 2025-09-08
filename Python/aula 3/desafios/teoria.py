# Curso Python #07 - Operadores Aritméticos
# 5+1==6
# 5-2==3
# 5*3==15
# 5/4==1.25
# 5**5==25
# 7//3==2 <-----------> 7|3
# 5%2==1                1|2

# + ADIÇÃO
# - SUBTRAÇÃO
# * MULTIPLICAÇÃO
# / DIVISÃO
# ** PONTÊNCIA
# // DIVISÃO INTEIRA
# % RESTO DA DIVISÃO

# ORDEM DE PROCEDÊNCIA
# 1.()
# 2.**
# 3.*././/.%
# 4.+.-

# EXEMPLO:
# 5+3*2== 11
# 3*5+4**2==31
# 3*(5+4)**2==243

# print('='*20)

# nome = input('Qual é o seu nome?')
# print(f'Prazer em te conhecer {:>20}'!)
# MAS NÃO FUNCIONOU O CÓDIGO ACIMA

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s=n1+n2 
sub=n1-n2
d=n1/n2
m=n1*n2
di=n1//n2
e=n1**n2
print('A soma vale é {},\n o subtração é {:.3f}\n e a divisão é {:.3f}'.format(m, s, d), end=' ')
print(f'Divisão inteira {d} \ne subtração inteira {sub}')