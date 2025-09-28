nomes = []
idades = []
sexos = []
maiorIdade = 0
soma = 0
cont = 0
for pessoa in range(1, 5):
    print("-" * 5, end="")
    print("{}ª PESSOA".format(pessoa), end="")
    print("-" * 5)

    nome = str(input("NOME: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

    if sexo == "M":
        if pessoa == 1:
            indexMaiorIdade = pessoa - 1
            maiorIdade = idade
        else:
            if idade > maiorIdade:
                indexMaiorIdade = pessoa - 1
                maiorIdade = idade

    if sexo == "F":
        if idade < 20:
            cont += 1
    soma += idade
media = soma / pessoa

if cont > 1:
    plural1 = "são"
    plural2 = 'es'
else:
    plural1 = "é"
    plural2 = ""
print("A média de idade do grupo é de {} anos\n"
      "O homem mais velho tem {} anos e se chama {}\n"
      "Ao todo {} {} mulher{} com menos de 20 anos".format(media,
                idades[indexMaiorIdade],
                nomes[indexMaiorIdade], plural1, cont, plural2))