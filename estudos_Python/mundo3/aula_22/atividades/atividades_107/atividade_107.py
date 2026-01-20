'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas 
aumentar(), diminuir(), dobro() e metade(). Faça também um programa 
que importe esse módulo e use algumas dessas funções.
'''

#Resposta

import modulo_moeda

Digite_valor = int(input('Digite o valor do salário: '))

aumentar = modulo_moeda.aumentar(Digite_valor)
diminuir = modulo_moeda.diminuir(Digite_valor)
dobro = modulo_moeda.dobro(Digite_valor)
metade = modulo_moeda.metade(Digite_valor)

print(f'A metade de {Digite_valor}: {metade}.')
print(f'O dobro de {Digite_valor}: {dobro}.')
print(f'Aumentando 10% de {Digite_valor}: {aumentar}.')
print(f'Diminuindo 10% de {Digite_valor}: {diminuir}.')