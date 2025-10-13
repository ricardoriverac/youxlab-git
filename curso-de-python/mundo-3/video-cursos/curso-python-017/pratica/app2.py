numero = [2, 5, 9, 1]
numero[2] = 3 #Substitui o número 9 pelo 3
numero.append(7) #Adiciona o número 7 no final da lista
numero.sort(reverse=True) #Coloca os números em ordem (reverse=True, inverte a ordem)
numero.insert(2, 2) #Adicionou o número 2 na posição 2
numero.remove(2) #Removeu o primeiro número 2 que apareceu na lista
print(numero)
print(f'Essa lista tem {len(numero)} elementos.')