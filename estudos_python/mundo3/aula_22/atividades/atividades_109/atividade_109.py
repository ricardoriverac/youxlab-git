'''

'''

#Resposta
import modulo_atividade_109
from modulo_atividade_109 import formatação

Digite_valor = int(input('Digite o valor do salário: '))

aumentar = modulo_atividade_109.aumentar(Digite_valor)
diminuir = modulo_atividade_109.diminuir(Digite_valor)
dobro = modulo_atividade_109.dobro(Digite_valor)
metade = modulo_atividade_109.metade(Digite_valor)

print(f'A metade de {modulo_atividade_109.metade(Digite_valor, True)}: {modulo_atividade_109.metade(metade,True)}.')
print(f'O dobro de {formatação(Digite_valor)}: {formatação(dobro)}.')
print(f'Aumentando 10% de {formatação(Digite_valor)}: {formatação(aumentar)}.')
print(f'Diminuindo 10% de {formatação(Digite_valor)}: {formatação(diminuir)}.')