#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


palavras = ('batata','carro','janela','vizinha','mochila','touca','celular')
for palavra in palavras:
   vogais_encontradas = []
   for letra in palavra:
       if letra.lower() in 'aeiou':
           vogais_encontradas.append(letra)
   print(f'A palavra {palavra} tem as vogais: {vogais_encontradas}')
