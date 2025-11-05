#Modulos

#O que é modulos??
'''
Um módulo é um arquivo Python (.py) que 
contém funções, variáveis, classes ou código 
que você pode reutilizar em outros programas.

👉 Em outras palavras: é uma forma de organizar e reaproveitar código.
'''

#Para que usar módulos
'''Imagina que você escreveu várias funções úteis num projeto — tipo funções matemáticas, de entrada de dados, etc.
Em vez de copiar e colar essas funções em cada novo programa, você pode colocar tudo num módulo e importar quando quiser.

Assim:

-> Seu código fica organizado.

-> Você evita repetição.

-> Facilita manutenção e leitura.'''

#Exemplo
import soma
n = soma.soma(1, 2)
print(n)