#Divisão

#contexto
palavra = 'Curso em video python'

#palavra.split()

'''
Esse comando corta onde tem o caractere que o usuario 
escolheu.O ususario pode escolher o caractere colocando o 
entre aspas dentro do parentese
'''
#Exemplo
'''
[Bom] [Dia]
  1     2  
'''


#'-'.join(palavra)
'''
O comanda junta as divisorias feita pelo "split"
e coloca qualquer catactere dentro das aspas no 
lugar do espaço
'''
#Exemplo
#print(' '.join(palavra))
#print('-'.join(palavra))
n1 = (palavra.split())
n2 = ('-'.join(n1))
print(n1)
print(n2)