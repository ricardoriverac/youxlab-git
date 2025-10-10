nome = str(input("digite seu nome: "))
ano_de_nascimento = int(input("digite seu ano de nascimento: "))
carteira_de_trabalho = int(input("digite o numero da sua carteira de trabalho: "))
idade = 2025 - ano_de_nascimento

if carteira_de_trabalho != 0:
    ano_de_contrataçao = int(input("digite o ano de contrataçao: "))
    salario = float(input("digite seu salario: "))
    idade_aposentadoria = ano_de_nascimento + 62
    dicionario = {'idade': idade,"nome":nome,"carteira_de_trabalho": carteira_de_trabalho, "salario":salario,"idade de aposentadoria":idade_aposentadoria}
else:
    dicionario = {'idade': idade,"nome":nome,"carteira_de_trabalho": carteira_de_trabalho,}
print(dicionario)    