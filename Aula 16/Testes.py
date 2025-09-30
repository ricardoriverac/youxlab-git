#tuplas: 
'''lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')'''

'''for comida in lanche:         #se não precisar mostrar a posição
    print(f'Eu vou comer {comida}')


for pos, comida in enumerate (lanche):    #repetição
   print(f'Eu vou comer {comida} na posição {pos}')    # pra mostrar a posição


#print(len(lanche))



for cont in range(0, len(lanche)): 
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') ''' # para mostrar a posição 




'''print(lanche)''' #vai mostrar tudo
'''print(lanche[1])'''
'''print(lanche[3])'''
'''print(lanche[-1])'''
'''print(lanche[-2])
print(lanche[1:4])
print(lanche[2:])
print(lanche[-2:])
print(lanche[-3:])'''

#tuplas são imutáveis
'''lanche[1] ='Refrigerante' '''#não consigo atribuir valores
'''print(lanche[1])'''


'''print(sorted(lanche))    # para colocar em ordem 
print(lanche)'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(len(c))
print(c.count(5))   # quantas vezes o 5 aparece
print(c.index(8))


'''print(a)
print(b) 
print(c)'''