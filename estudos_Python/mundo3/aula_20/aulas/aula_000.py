#Funções(parte 1)

#Como utilizar a função def
'''
Para criar uma função em Python, você precisa escrever a 
palavra-chave def, seguida do nome da função, depois os 
parênteses () e, em seguida, dois pontos :.

Na linha de baixo, escreva o código da função com a indentação 
correta (geralmente quatro espaços).
'''
#Exemplo

def saudacao():
    print("Olá, mundo!")

#Como chamar uma função def
'''
depois que você define uma função com def, você pode 
chamá-la simplesmente escrevendo o nome da função 
seguido de parênteses.
'''
#Exemplo
saudacao()

#O que e parâmetro
'''
Em Python, um parâmetro é uma variável que aparece na definição de 
uma função — ela serve para receber valores (argumentos) quando a 
função é chamada.
'''
#Exemplos
def saudacao(nome):
    print(f"Olá, {nome}!")

'''
nome é o parâmetro da função saudacao.
Quando você chama a função, passa um argumento 
(um valor real) para esse parâmetro.
'''

saudacao("Otto")

#Como adicionar varios números em um parâmetro
'''
Para isso, quando for declarar o parâmetro,
você deve colocar um '*', isso faz que o python coloque
todos os números dentro de um parâmetro
'''
#Exemplo
def soma(*soma):
    print(f'Resultado - {sum(soma)}')

soma(1, 45, 7, 19, 12 ,1)

