#Escopo de variáveis

#Escopo global

'''
Uma variável global é criada fora de funções e pode ser acessada em qualquer 
parte do código (inclusive dentro de funções, se não for sobrescrita).
'''

#Escopo local
'''
Uma variável local é criada dentro de uma função e só existe dentro dela.
Fora da função, ela não é reconhecida.
'''

#Exemplo

def soma(valor):
    valor1 = 5 #Escopo Local
    r = valor1 * valor
    print(r)


valor2 = 6 #Escopo Global
soma(valor2)

#Como utilizar o global
'''
No python pode existir 2 variáveis com o 
mesmo nome, uma global e a outra local
'''
#Exemplo
def soma():
    re = 1 + 2 #Variável local
    print(re)
re = 78 #Variável global
soma() #O resulatdo e 3

'''
Um valor não interfere no outro, pois as 
duas são variáveis diferente, mas para eu
conseguir utilizar o valor da global dentro 
de uma função def, e isso só pode ser possivel
com o comando global
'''
#Exemplo
def soma():
    global resul
    r = 1 + 2 #Variável local
    print(resul)
resul = 78 #Variável global
soma() #O resultado e 78
