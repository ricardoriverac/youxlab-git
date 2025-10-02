#aula 13 - ESTRUTURA DE CONTROLE

#EXPLICAÇÃO TEORICA

#comando laço : repete um bloco de código,voce consegue impor um limite começa do 0 e vai ate o final,se eu por 1-5 ele vai começa do  1 e vai para no 5   

#PRIMEIRO EXEMPLO 
#laço c no intervalo(1,10)
#    passo
#pega 
#como escrever isso no python 
#or c in rangel(0,3):
#if moeda:
#   passo
#   pula
#passo   
#pega    
 
#AULA PRATICA 
#for c in range(1,6)
#    print("oi")
#print("fim")

#for c in range(1,7)
#     print(c)
#print("fim")  
#for c in range(0,6,2):  #(-1)#escreve de traz pra frente
#    print(c)
#print("fim")  


##
# for c in range (0,n+1):
##print("fim")   

inicio = int(input("inicio: ")) 
fim = int(input("fim:"))
passos = int(input("passo"))
for c in range (inicio,fim+1,passos):
    print(c)
print("fim")    