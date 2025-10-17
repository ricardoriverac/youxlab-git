from Utilidades.moeda import moeda
from Utilidades.indentificador import tester

num = str(tester.readNumber('Digite o preço:'))
print(moeda.moneyator(num))