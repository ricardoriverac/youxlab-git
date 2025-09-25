# Curso Python #013 - Estrutura de repetição for
# laço c no intervalo(1, 10) ========traduzindo...========= for c in rangel(1, 10):
# laço c no intervalo(0, 3) ========traduzindo...========= for c in rangel(0, 3):
# laço c no intervalo(0, 3) ========traduzindo...========= for c in rangel(0, 3):
#    se @ >>ex.: de moeda                                  if @:
# PRÁTICA
# for c in range(0, 6):
#     print('Oi')
# print('FIM')
# =======repete a palavra 6 vezes ============
# for c in range(0, 6):
#     print('c')
# print('FIM')
# ===========vai em ordem númerica ============
# for c in range(6, 0, -1):
#     print('c')
# print('FIM')
# ==========contagem regressiva================
#  for c in range(0, 7, 2):
#     print('c')
# print('FIM')
# ===========pula de dois em dois===============

# TESTE 1
# numero = int(input('Digite um número: '))
# for c in range(0, numero + 1):
#     print(c)
# print('FIM')
# TESTE 2 
# inicio = int(input('Início: ')) # determina o inicio
# fim = int(input('Fim: ')) # determina o final das casas
# passo = int(input('Passo: ')) # conta de quantas em quantas casas vai pular ex.: de 10 em 10 ou de 2 em 2
# for c in range(inicio, fim + 1, passo):
#     print(c)
# print('FIM')
# TESTE 3
# for c in range(0, 3):
#     valor = int(input('Digite um valor: '))
# print('FIM')
# ==========quantidade de vezes que repete a frase==========
# TESTE 4
soma = 0
for c in range(0, 3):
    valor = int(input('Digite um valor: '))
    soma += valor 
print(f'O somátorio de todos os valores foi {soma}')
#
#
#
#
#
#
#
#
#
#