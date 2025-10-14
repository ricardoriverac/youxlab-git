#Importando a função 'sleep' do módulo time, me permitindo pausar a execução do código por um certo número de segundos.
from time import sleep

#Importando o módulo random, usado para gerar números aleatórios.
import random

# o programa está perguntando quantos jogos ele quer gerar.
jogo = int(input('Quantos jogos você quer que eu sorteie? '))

#Inicia aqui um laço de repetição que vai de 0 até jogos - 1.
# (ex:Se o usuário digitou 5, por exemplo, o range(5) vai repetir 5 vezes, ou seja, sortear 5 jogos.
for j in range(jogo):

#Essa linha sorteia 6 números aleatórios de 0 a 59 (lembrando que range(60) vai de 0 até 59).
#A função random.sample(x,x) não repete números.
    numeros = random.sample(range(60), 6)

#Organizando os números sorteados em ordem crescente.
    numeros.sort()

#Faz o programa esperar 1 segundo antes de continuar, para simular um sorteio com mais "suspense".
    sleep(1)

#resultado:
    print(f'Jogo {j+1}: {numeros}')