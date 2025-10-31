#DOCSTRINGS

'''
Um  DOCSTRINGS e uma forma de ver a funcionalidade
da propria função que você criou no codigo
'''
'''
Para isso, vc dever abrir aspas triplas bem de baixo 
do def, ai dentro dessas aspas tripas você coloca a 
descrição da funcionalidade
'''
#Exemplo
def par_impar(numero):
    '''
    Funcionalidade: A função par_impar serve
    para ver se um número e PAR ou IMPAR

    Como usar: Você deve colocar o número 
    que deseja verificar dentro dos ()

    Exemplo: par_impar(4)
    '''
    if numero % 2 == 0:
        print(f'{numero} - Par')
    else:
        print(f'{numero} - Impar')

par_impar(int(input('par_impar: ')))

help(par_impar)