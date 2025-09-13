#Como baixar bibliotecas

'''
Na linguagem python, para incluir alguma biblioteca
e necessario utilizar o comando "import" 
'''

#Exemplo                   (OBS: a biblioteca "math"  e só um exemplo)
                               
import math

'''
Tudo dentro da biblioteca sera importado para o codigo 
'''

#Como importar funções expecificas da biblioteca

'''
Esse comando importa funções expecificas
da biblioteca, é não todas de uma vez
'''

#Exemplo

from math import floor

'''
Mas para importar mais que uma função, mas não todas 
de uma vez, você devera utilizar a virgula 
'''

#Exemplo

from math import pow , sqrt 

#Adicionar uma função no codigo 

'''
Para adicionar uma função no codigo você devera 
colocar o nome da biblioteca um ponto na frente 
e depois o nome da função


Se somente as funções forem adicionadas, não 
sera necessario utilizar o " math."
'''

#Exemplo

raiz_quadrada = sqrt(4)
operações = pow(3,2)
