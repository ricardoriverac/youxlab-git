numero = [2, 5, 9, 1]
numero[2] = 3 #Substitui o número 9 pelo 3
numero.append(7) #Adiciona o número 7 no final da lista
numero.sort(reverse=True) #Coloca os números em ordem (reverse=True, inverte a ordem)
numero.insert(2, 0) #Na posição [2] foi adicionado o número 0
numero.pop(2) #Elimina o último número (pop(2) elimina o segundo número da lista, no caso o número 2)
print(numero)
print(f'Essa lista tem {len(numero)} elementos.')