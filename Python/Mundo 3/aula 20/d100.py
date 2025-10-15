from random import randint
from time import sleep # faz o código "dormir" pela quantidade de segundos que eu quiser.

print('-'*60)
print('                  SORTEANDO NÚMEROS    ')
print('-'*60)
def sorteia(lista):
    print('-- Sorteando 5 números da lista: ', end='') # Mostra no terminal uma mensagem, mas com end='' ele não pula de linha, fica tudo na mesma linha.

    for contador in range(0, 5):# Cria um loop que roda 5 vezes, porque queremos sortear 5 números.
                        # contador vai de 0 a 4.

        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True) # flush=True faz o texto aparecer imediatamente (sem atraso do sistema).
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista: 

        if valor % 2 == 0: #Verifica se o número é par.
                           #O % é o operador de módulo (pega o resto da divisão).
                           #Se o resto da divisão por 2 for 0, então o número é par.

            soma += valor
    print(f'    Somando os valores pares de {lista}, temos {soma}.')  #O print() está dentro do for, então ele imprime o resultado várias vezes,
                                                                      # imprimindo uma vez para cada número que foi sorteado da lista eso ele não sendo PAR

numeros = []
sorteia(numeros)
somaPar(numeros)
print('-'*60)