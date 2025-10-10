'''#Listas: Variaveis compostas
#Nâo é possível mudar as tuplas

#Tuplas = ( )               Listas = [ ]

#Jeito certo de modificar um elemento:
lanche = [' oi ', ' não ', ' sim ']
lanche[2] = ' programaçao '

#Jeito errado: 
lanche = ('oi', 'não', 'gato')
lanche (0) = 'sim'

#Listas podem ser modificadas, tuplas não podem ser modificadas.

lanche.append (' ')
#É usado para adicionar elementos no final da lista

lanche.insert(0, ' ')
#É usado para adicionar elementos no inicio da lista

#Como apagar elementos:

del lanche [3]
ou lanche.pop() #Esse é mais usado para apagar o ultimo elemento

lanche.remove(' ')
#Esse não indica posição, indica o valor/o que quero deletar entre aspas.

#Como conferir se um elemento existe para ser deletado sem dar erro no programa.
if ' ' in lanche:
    lanche.remove (' ')

#Organizar elementos: 
valores = [3,1,2,6,10,9]
valores.sort()
resultado : valores = [1,2,3,6,9,10]

#Para inverter a ordem: 
valores = [8,2,5,4,9,3,0]
valores.sort()
valores.sort(reverse = True)

#Como saber o tamanho da lista:
valores = [8,2,5,4,9,3,0]
len(valores)

resultado = 7'''
