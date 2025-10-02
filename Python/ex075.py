# O laço 'for' irá repetir o bloco de código 5 vezes
for i in range(5):
    # 'input()' pede uma entrada do usuário
    pergunta = input(f"Pergunta {i+1} de 5: Qual é o seu nome? ")
    # 'f"..." ' permite formatar a string com variáveis
    print(f"Olá, {pergunta}! ")
