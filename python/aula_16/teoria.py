# maneiras de usar tuplas 
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# 1
for comida in lanche:
    print(f'Eu vou comer {comida}')
# 2
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
# 3
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

# colocar ordenado 
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche))

# posição
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(8))

# apagar variavel
pessoa = ('Ana Laura', 16, 'F', 52.00)
del(pessoa)
print(pessoa)