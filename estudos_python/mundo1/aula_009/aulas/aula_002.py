#Análise

#contexto

palavra = str('   Curso em video python    ')

#len(exemplo)

'''
len(exemplo)

Esse comando e utilizado para medir o comprimento da frase
'''
#Exemplo
print(len(palavra))

#frase.count('e')

'''
Esse comando e utilizado para contar quantas 
letras (exemplo: e) tem na frase

Também tem que ser expecificado se a letra e maiuscula 
ou minusculo.Pois se a letra for maiuscula o comando 
só ira procurar a letra em maiuscula, e a mesma regra
se a letra estiver em minuscula
'''
#Exemplo
print(palavra.count('e'))

#frase.count('e',0,13)

'''
O comando "frase.count('e',0,13)"  mostra a quantia de
letras já com fatiamento
'''
#exemplo
print(palavra.count('e',0,21))

# exemplo in frase

'''
O comando " in " e utilizado para saber se tem 
uma determinada palavra na variavel
'''

'''
Para utilizar o comando o usuario devera colocar a palavra
que deseja que seja verificada na variavel, depois o " in "
e em seguida o nome da variavel que deseja que seja verificada 
'''

#Exemplo
print('ta_maluco' in palavra)

#frase.replace('Python' , 'exemplo')

'''
O comando substitui palavras ou letras. A segunda e a qual vai ser
substituida, e a primeira palavra e a que vai ser substituida
'''
#Exemplo
print(palavra.replace('python' , 'q'))

#frase.upper() é fraser.lower()

'''
"upper()" mantem as maiusculas e substitui as letras minusculas para maiusculas
'''
#Exemplo
print(palavra.upper())

'''
"lower()" ,antem as minusculas e substitui as letras maiusculas por minusculas
'''
#Exemplo
print(palavra.lower())

#frase.capitalize() é frase.title()

'''
o "capitalize()  pega a string, joga ela para minuscula e a primeira letra em maiuscula
'''
#Exemplo
print(palavra.capitalize())

'''
o "title", deixa as primeiras letras das palavras dentro da string maiusculas
'''
#Exemplo
print(palavra.title())

#frase.strip()

'''
Ele remove os espaço inuteis da string, como os espaço antes da primeira letra
e os espaço depois da utima letra
'''
#Exemplo
print(palavra.strip())

#frase.rstrip()

'''
Só remove os espaço depois da ultima letra
'''
#Exemplo
print(palavra.rstrip())


#frase.lstrip()

'''
Remove os espaço antes da primeira palavra da string
'''
#Exemplo
print(palavra.lstrip())

#frase.find e frase.rfind

'''
O "find" procura algum caractere de uma string a partir do lado esquerdo
'''

'''
O "rfind" procura algum caractere na string do lado direito
'''
#exemplo

#find
print(palavra.find('o'))

#rfind
print(palavra.rfind('o'))