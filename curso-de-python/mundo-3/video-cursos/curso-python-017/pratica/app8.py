a = [2, 3, 4, 7]
b = a[:] # O 'b' receberá os mesmo valores que 'a', mas não terá uma ligação entre as duas listas. Ex: b = a (Conexão), b = a[:] (Copia dos valores de 'a' para 'b')
b[2] = 8

print(f'Lista A {a}')
print(f'Lista B {b}')