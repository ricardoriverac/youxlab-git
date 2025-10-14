#Laços de repetição(parte 1)

#Laço com variavel de contrle

'''
Essa função faz que um codigo consiga repetir infinitamente 
ate onde o usuario  determinar, e depois o codigo continuara
 normalmente
'''
'''
obs:swe colocar " , -1 " e inverter os números ele vai contar de trás para frente
'''


#Exemplo

print('Começo:')
for c in range(9,0, -1):
    print(c)
print('Fim:')

#Exemplo 2 

n = int(input('Digite um número: '))

for c in range(0, n):
    print(c)