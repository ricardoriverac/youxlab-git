#listas sao mutaveis
#append () vai adicionar elementos ao final da minha lista
#insert () permite adicionar um único elemento em uma posição específica dentro da lista
#del lanche [3] vai eliminar oq eu qro eliminar
#lanche.pop(3) geralmente vai apagar o ultimo valor da lista
#remove - remove direto pelo nome da str ou valor
#posso usar list para declarar listas
#valores.sort() vai ordenar os valores da lista
#sort(reverse=True) vai oedenar de tras para frente
valores = []
valores.append(5)
valores.append(7)
valores.append(4)
for c,v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista ')    