# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

minha_list = []
for c in range(0,5):
    valores = int(input('Digite um valor: '))
    if len(minha_list) == 0 or valores > minha_list[-1]:
      minha_list.append(valores)
    else:
        pos= 0
        while pos < len(minha_list):
            if valores <= minha_list[pos]:
                minha_list.insert(pos, valores)
                break
            pos += 1
print(f'Os valores digitados em ordem:{minha_list}')
