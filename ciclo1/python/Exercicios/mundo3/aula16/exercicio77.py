palavras = ()

for i in range(3):
    texto = str(input(f"Escreva a {i+1}ª palavra [sem acentos]: "))
    palavras += (texto,)

for c in palavras:
    vogais = ""
    for caractere in c:
        if caractere == "a":
            vogais += " " + "a"
        elif caractere == "e":
            vogais += " " + "e"
        elif caractere == "i":
            vogais += " " + "i"
        elif caractere == "o":
            vogais += " " + "o"
        elif caractere == "u":
            vogais += " " + "u"
    print(f"A palavra {c} possui as vogais: {vogais}")



