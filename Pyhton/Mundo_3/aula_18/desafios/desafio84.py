pessoas = list()
#criei uma lista vazia
dados = list()
# criei outra lista vazia
maior = 0
menor = 0
cont = 0
#criei três variaveis maio: maior peso / menor: menor peso / cont: pessoas cadastradas
while True: # repetição / só para quando eu usar o break
    dados.append(str(input("Digite o nome: ")))
    dados.append(float(input("Digite o peso: ")))
    #pede pra digitar o nome e o peso e guarda na lista dados
    if len(pessoas) == 0:
        maior = menor = dados[1]
        #para descobrir o maior peso e o menor
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
            #compara os pesos e vai atualizando
    pessoas.append(dados[:])
    # guarda todos os dados e continua o código / copia os dados e coloca na lista 'pessoas'
    cont = cont + 1
    #para aumentar o contador de pessoas cadastradas
    dados.clear()
    #limpando a pasta dados para eu usar ela de novo
    resposta = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    # perguntando se quero continuar / o comando '.upper()' deixa a letra maiuscula / '.strip()' tira todos os espaços /
    # [0] vai pegar só a letra inical
    while resposta not in "SN":
        print("Opção inválida! Tente novamente.")
        resposta = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        #se digitar algo que não seja s ou n, da erro e tem que responder denovo.
    if resposta == "N":
        break
    #se digitar n o break para e sai do loop.
print(f"Pessoas cadastradas: {cont}.")
#quantas pessoas cadastradas
print(f"Maior peso: {maior}Kg. Peso de ", end='')
#Maior peso
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}]", end=' ')
        # passa de pessoa em pessoa e mostra o nome de quem tem o maior peso.
print()
#pula pra proxima linha
print(f"Menor peso: {menor:.2f}Kg. Peso de ", end='')
#Mostra o menor peso (com 2 casas decimais).
for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}]", end=' ')
        #mostra o nome de quem tem o menor peso.