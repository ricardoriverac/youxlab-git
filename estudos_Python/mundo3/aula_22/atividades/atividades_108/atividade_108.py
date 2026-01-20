'''
Adapte o código do desafio #107, criando uma função adicional chamada 
moeda() que consiga mostrar os números como um valor monetário formatado.
'''

#Resposta

import modulo_atividade_108
from modulo_atividade_108 import formatação

Digite_valor = int(input('Digite o valor do salário: '))

aumentar = modulo_atividade_108.aumentar(Digite_valor)
diminuir = modulo_atividade_108.diminuir(Digite_valor)
dobro = modulo_atividade_108.dobro(Digite_valor)
metade = modulo_atividade_108.metade(Digite_valor)

print(f'A metade de {formatação(Digite_valor)}: {formatação(metade)}.')
print(f'O dobro de {formatação(Digite_valor)}: {formatação(dobro)}.')
print(f'Aumentando 10% de {formatação(Digite_valor)}: {formatação(aumentar)}.')
print(f'Diminuindo 10% de {formatação(Digite_valor)}: {formatação(diminuir)}.')