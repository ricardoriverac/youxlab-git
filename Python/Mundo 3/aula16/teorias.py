lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in range:
    print(f'Eu vou comer{comida}!')

for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador}')

for posicao, comida in enumerate(lanche):
   print(f'Eu vou comer {comida} na posição {posicao}')

print('Comi pra caramba!')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(2, 1))