print('-'*30)
print('    TEORIAS PARTE 1')
#def soma(a, b):
#    print(f'A = {a} e B = {b}.')
#    s = a + b
#    print(f'A soma de A + B = {s}')


#soma(a=4, b=5)
#soma(7, 2)

print('-'*30)
print('    TEORIAS PARTE 2')
print('    COMO EMPACOTAR: ')

#def contador(* num):
#    tam = len(num)
#    print(f'Recebi os valores {num} e são ao todo {tam} números.')


#contador(2, 1, 7)
#contador(8, 0)
#contador(4, 4, 7, 6, 2)

print('-'*30)
print('    TEORIAS PARTE 3')
print('     USANDO DEF COM LISTAS')
def dobra(lst):
    posicao = 0
    while posicao < len(lst):
        lst[posicao] *= 2
        posicao += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
