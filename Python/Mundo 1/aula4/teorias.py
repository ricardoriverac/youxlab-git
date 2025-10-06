print('Olá, Mundo!')
print(7+4)
print('7'+'4')
print('Olá' , 5)

nome = 'Luis'
idade = 15
peso = 43.2
print(nome, idade, peso)

nome = str(input('Qual é o seu nome? '))
idade = int(input('Quantos anos você tem? '))
peso = float(input('Quantos você pesa? '))
print(nome, idade, peso)

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))

Dia = int(input('Dia = '))
Mês = str(input('Mês = '))
Ano = int(input('Ano = '))
print('Você nasceu no dia ',Dia,' de ',Mês,' de ',Ano,'. Correto?')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('A soma é: ' , n1 + n2)