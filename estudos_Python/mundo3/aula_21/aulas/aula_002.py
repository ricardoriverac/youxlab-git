#Parâmetros opsionais

'''
Um parâmetro opcional é um parâmetro de função que tem um valor padrão.
Ou seja, se você não passar nada pra ele, o Python usa esse valor padrão automaticamente.
'''
#Exemplo
def multplicador(multpli1, multipli2 = 2):
    r = multpli1 * multipli2
    print(f'{multpli1} * {multipli2} = {r}')

multplicador(5)

'''
No exemplo acima somente o multpli1 recebeu valor, já o 
multpli2 não recebeu valor, então ele recebeu o
valor base dele (que e 2)
'''