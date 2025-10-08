# from datetime import date
# ano_atual= date.today().year
# ano_nascimento = float(input('Pessoa 1, digite seu ano de nascimento: '))
# print(ano_atual - ano_nascimento)
# idade = ano_atual - ano_nascimento
# if idade> 18:
#     print('Você é maior de idade')
# else:
#     print('Você é menor de idade ')
# ano_nascimento = float(input('Pessoa 2, digite seu ano de nascimento: '))
# print(ano_atual - ano_nascimento)
# idade = ano_atual - ano_nascimento
# if idade> 18:
#     print('Você é maior de idade')
# else:
#     print('Você é menor de idade ')
# ano_nascimento = float(input('Pessoa 3, digite seu ano de nascimento: '))
# print(ano_atual - ano_nascimento)
# idade = ano_atual - ano_nascimento
# if idade> 18:
#     print('Você é maior de idade')
# else:
#     print('Você é menor de idade ')
# ano_nascimento = float(input('Pessoa 4, digite seu ano de nascimento: '))
# print(ano_atual - ano_nascimento)
# idade = ano_atual - ano_nascimento
# if idade> 18:
#     print('Você é maior de idade')
# else:
#     print('Você é menor de idade ')
# ano_nascimento = float(input('Pessoa 5, digite seu ano de nascimento: '))
# print(ano_atual - ano_nascimento)
# idade = ano_atual - ano_nascimento
# if idade> 18:
#     print('Você é maior de idade')
# else:
#     print('Você é menor de idade ')
# ano_nascimento = float(input('Pessoa 6, digite seu ano de nascimento: '))
# print(ano_atual - ano_nascimento)
# idade = ano_atual - ano_nascimento
# if idade> 18:
#     print('Você é maior de idade')
# else:
#     print('Você é menor de idade ')
# ano_nascimento = float(input('Pessoa 7, digite seu ano de nascimento: '))
# ano_atual = float(input('Digite o ano atual: '))
# print(ano_atual - ano_nascimento)
# idade = ano_atual - ano_nascimento
# if idade> 18:
#     print('Você é maior de idade')
# else:
#     print('Você é menor de idade ')


from datetime import date
contadorMaiorIdade = 0
contadorMenorIdade = 0
ano_atual= date.today().year
for c in range (1, 5000000):
    ano_nascimento = float(input(f'Pessoa {c}, digite seu ano de nascimento: '))
    idade = ano_atual - ano_nascimento
    print(f"Sua idade é {idade}")
    if idade >= 18:
        contadorMaiorIdade += 1
    elif idade >= 0 and idade < 18:
        contadorMenorIdade += 1
print(f'Temos {contadorMaiorIdade} pessoas maiores de idade e {contadorMenorIdade} pessoas menores de idade.')