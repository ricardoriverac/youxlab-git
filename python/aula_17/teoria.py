# listas são mutáveis (podem ser alterados)
numero = [2, 5, 9, 1]
numero[2] = 3
print(numero)

# adicionando um valor 
numero = [2, 5, 9, 1]
numero[2] = 3
numero.append(7)
print(numero)

# colocar na ordem (em ordem decrescente é só usar "reverse=True" no "()")
numero = [2, 5, 9, 1]
numero[2] = 3
numero.append(7)
numero.sort()
print(numero)

# contar elementos
numero = [2, 5, 9, 1]
numero[2] = 3
numero.append(7)
print(numero)
print(f'Essa lista tem {len(numero)} elementos. ')

# inserir valores
numero = [2, 5, 9, 1]
numero[2] = 3
numero.append(7)
numero.sort
numero.insert(2, 0)
print(numero)
print(f'Essa lista tem {len(numero)} elementos. ')

# excluir elemento
umero = [2, 5, 9, 1]
numero[2] = 3
numero.append(7)
numero.sort
numero.insert(2, 0)
numero.pop(2)
print(numero)
print(f'Essa lista tem {len(numero)} elementos. ')
