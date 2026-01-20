#Variaveis composta(lista parte 2)

#Como colocar uma lista dentro da outra
'''
Uma lista composta e uma lista feita de outras listas
'''
#Exemplo

nome_e_idade = [['Maria' , 25] , ['Joao' , 13] , ['Luiz' , 45]]

'''
Você pode acessar as listas que estão dentro  os conteudos
que estão dentro das listas. Mas para isso necessario utilizar 
os seguintes comando:
'''

#Acessar a lista segundaria
'''
Se você quizer mostras a lista inteira você abre um couchetes na frente do nome 
da lista principal, e dentro do couchetes coloca o indece que representa aquela lista segundaria
'''
#Exemplo
print(nome_e_idade[0])

#Como acessar um valor especifico dentro da lista segundaria
'''
Pra acessar um valor especifico dentro das listas, você pode colocar um segundo
couchets na frente do primerio, e nesse segundo couchetes você tem que colocar
o indece do valor que esta dentro da lista segundaria
'''
#Exemplo
print(nome_e_idade[2][1])

'''
O 1° couchetes representa qual lista deseja acessar, e o 2° couchets e para acessar 
o indecer dentro da lista segundaria
'''