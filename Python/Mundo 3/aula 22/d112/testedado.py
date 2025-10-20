from d112.utilidadescev import moeda
from d112.utilidadescev import dado

preco = dado.leiadinheiro('Digite o preço: R$')
moeda.resumo(preco, 20, 12)