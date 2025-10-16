print('-'*30)
print('     TEORIAS PARTE 1')
print()
#print(input.__doc__)
#help(input)
 
print('-'*30)
print('     TEORIAS PARTE 2')
print('     DOCSTRINGS')
print()
#def contador(inicio, fim, passo):
#    """ 
#    -> Faz uma contagem e mostra na tela.
#    :parametro inicio: inicio da contagem
#    :parametro fim: fim da contagem
#    :parametro passo: de quanto em quanto está indo
#    :return: sem retorno
#    """
#    c = inicio
#    while c <= fim:
#        print(f'{c} ', end='')
#        c += passo
#    print('FIM...')

#contador(2, 10, 2)
#help(contador)

print('-'*30)
print('     TEORIAS PARTE 3')
print('     PARÂEMTROS OPCIONAIS')
print()
#def somar(a, b, c):
#    """
#    -> Faz a soma dos três valores e mostra o resultado na tela.
#    :parametro a: o primeiro valor 
#    :parametro b: o segundo valor
#    :parametro c: o terceiro valor
#    """
#    s = a + b + c
#    print(f'A soma dos valores {a} + {b} + {c} = {s}')#####

#somar(3, 2, 5)
#print()
#print('     SEGUNDA PARTE')
#print()
#def somar(a, b, c=0): # C é um parâmetro opcional.
#    """
#    -> Faz a soma dos três valores e mostra o resultado na tela.
#    :parametro a: o primeiro valor 
#    :parametro b: o segundo valor
#    :parametro c: o terceiro valor
#    """
#    s = a + b + c
#    print(f'A soma dos valores {a} + {b} + {c} = {s}')

#somar(3, 2)
#print()
#print('     TERCEIRA PARTE')
#print()
#def somar(a, b=0, c=0): # B e C são parâmetros opcionais.
#    """
#    -> Faz a soma dos três valores e mostra o resultado na tela.
#    :parametro a: o primeiro valor 
#    :parametro b: o segundo valor
#    :parametro c: o terceiro valor
#    """
#    s = a + b + c
#    print(f'A soma dos valores {a} + {b} + {c} = {s}')

#somar(3)
#print()
#print('     QUARTA PARTE')
#print()

#def somar(a=0, b=0, c=0): # A, B e C, são parâmetros opcionais.
#    """
#    -> Faz a soma dos três valores e mostra o resultado na tela.
#    :parametro a: o primeiro valor 
#    :parametro b: o segundo valor
#    :parametro c: o terceiro valor
#    """
#    s = a + b + c
#    print(f'A soma dos valores {a} + {b} + {c} = {s}')

#somar()

#def somar(a=0, b=0, c=0):# A, B e C, continuam sendo parâmetros opcionais
#    """
#    -> Faz a soma dos três valores e mostra o resultado na tela.
#    :parametro a: o primeiro valor 
#    :parametro b: o segundo valor
#    :parametro c: o terceiro valor
#    """
#    s = a + b + c
#    print(f'A soma dos valores {a} + {b} + {c} = {s}')

#somar(3, 2, 5, 4) #Para adicionar mais um valor terá que adicionar na função (def soma(*num)).

print('-'*30)
print('     TEORIAS PARTE 4')
print('     ESCOPO  DE VARIÁVEIS')
print()

#def teste(): # A função teste n recebu parâmetro nenhum.
#    x = 8
#    print(f'Na função teste, N vale {n}.')
#    print(f'Na função teste, X vale {x}.')
#PROGRAMA PRINCIPAL
#n = 2
#print(f'No programa principal, N vale {n}.') # A variável n funciona fora da função, pois foi declarada fora da função teste.
#teste() # Isso serve para chamar a função.
#print(f'No programa principal, X vale {x}.') # A variável x n funciona aqui, pois a variável x está dentro da função.

#print('-'*30)
#print('     PARTE 2')
#print()

#def funcao():
#    n1 = 4
#    print(f'N1 dentro da função vale: {n1}.')

#n1 = 2
#funcao()
#print(f'N1 fora da função vale: {n1}.')

print('-'*30)
print('     TEORIAS PARTE 5')
print('     RETORNANDO VALORES')
print()

#def somar(a=0, b=0, c=0): 
#    s = a + b + c
#    print(f'A soma dos valores vale: {s}.')

#somar(3, 2, 5)
#somar(2, 2)
#somar(5)


print('-'*30)
print('     PARTE 2')
print()

#def somar(a=0, b=0, c=0):
#    s = a + b + c
#    return s

#resp = somar(3, 2, 5)    
                      # Posso colocar dentro de uma variável 
                      # ou dentro de um print
#print(somar(3, 2, 5))

#r1 = somar(3, 2, 5)
#r2 = somar(1, 7)
#r3 = somar(4)
#print(f'Meus cálculos deram: {r1}, {r2} e {r3}.') # Dessa forma consigo colocar um print() formatado e mais organizado.

print('-'*30)
print('     TEORIAS PARTE 5')
print('     RETORNANDO VALORES')
print('     FATORAR NÚMEROS USANDO FUNÇÃO')
print()

def fatorial(num=1):
    fat = 1
    for cont in range(num, 0, -1):
        fat *= cont
    return fat # Não é só usado para números, podemos retornar um valor lógico (Verdadeiro, Falso)

#numero = int(input('Digite um número: '))
#print(f'O fatorial de {numero}, é igual a {fatorial(numero)}.')

#f1 = fatorial(5)
#f2 = fatorial(4)            #Forma para mais valores.
#f3 = fatorial()
#print(f'Os resultados são: {f1}, {f2} e {f3}.')

print('-'*30)
print('     PARTE 2')
print('     USANDO RETURN PARA VALORES LÓGICOS')
print()

#def par(n=0):
#    if n % 2 == 0:
#        return True
#    else:
#        return False
#    
#numero = int(input('Digite um número: '))
#print(par(numero)) #Primeira forma para mostrar se é par.

#if par(numero):
#    print('É par!')
#else:                   #Segunda forma para mostrar se é par ou ímpar.
#    print('Não é par!')

