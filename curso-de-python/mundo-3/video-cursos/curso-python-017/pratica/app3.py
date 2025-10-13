numero = [2, 5, 9, 1]
numero[2] = 3 #Substitui o número 9 pelo 3
numero.append(7) #Adiciona o número 7 no final da lista
numero.sort(reverse=True) #Coloca os números em ordem (reverse=True, inverte a ordem)
numero.insert(2, 2) #Adicionou o número 2 na posição 2

if 4 in numero: #Se ter um número 4 na lista, ele será removido, caso não tenha, o código só dirá que o número 4 não está na lista.
    numero.remove(4)
else:
    print('O número 4 não está na lista.')

print(numero)
print(f'Essa lista tem {len(numero)} elementos.')