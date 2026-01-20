'''
Cria um programa que leia o ano de nascimento de sete pessoas. 
No final, mostra quantas pessoas ainda não atingiram a maioridade a quantas já SÃO maiores.
'''

#Resposta
import datetime
data_atual = datetime.date.today()
ano_atual = data_atual.year
print(ano_atual)
n = 0
menor = 0
maior = 0


for c in range(1, 7):
    n = n+1
    ano_de_nascimento = int(input(f'Digite o {n}° ano de nascimento: '))
    if ano_atual- ano_de_nascimento < 18 :
        menor = menor + 1
    elif ano_atual - ano_de_nascimento >= 18 :
        maior = maior + 1
print(f'''A quantidade de pessoas menores de idade é: {menor}.
          E a quantidade de pessoas de maior é: {maior}. ''')

