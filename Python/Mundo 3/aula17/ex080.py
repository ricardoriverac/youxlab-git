# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção 
# (sem usar o sort()). No final, mostre a lista ordenada na tela.


valores = []
for c in range(5):
    valor = str(input(f'Digite um valor: '))
    if c == 0:
      valores.append(valor)
    else:
       for i in range(len(valores)):
          if valor < valores[i]:
                valores.insert(i, valor)
                break
          else:
                if i == len(valores)-1:
                    valores.append(valor)
print(valores)
   

    