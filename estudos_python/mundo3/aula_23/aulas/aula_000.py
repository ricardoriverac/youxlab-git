#Erros e Eceções

#Função try
'''
A função try serve para tratar erros que podem acontecer 
durante o seu codigo
'''

#Função except
'''
A palavra-chave except em Python serve para tratar o erro 
que pode acontecer dentro de um bloco try.
'''

#Função else
'''
Só mostra quando o código da certo
'''

#Função finally
'''
Mostra independente se o codigo deu certo
ou errado
'''

'''
Em outras palavras:
-> "try" tenta executar um código
-> "except" diz o que fazer se ocorrer um erro
-> "else" fala o que ocorre se der certo
-> "finally" ocorre independente se deu certo ou errado
'''

#Exemplo
try:
    n1 = int(input('Digite o 1° número: '))
    n2 = int(input('Digite o 2° número: '))

    # código que pode gerar um erro
    resultado = n1 / n2
except:
    # o que fazer se der erro
    print("Ocorreu um erro!")

else:
    #o que ocorre se der certo
    print(resultado)

finally:
    #ocorre independente se deu certo ou errado
    print('Volte sempre!!')
