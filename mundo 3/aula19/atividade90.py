nome = str(input("digite seu nome: "))
media1 = float(input(f"media de {nome}: "))
dicionario = {"nome": nome,"media": media1,}
print(f"o nome e igual a: {dicionario.get('nome')}")
print(f"a media e igual a: {dicionario.get('media')}")
if dicionario.get("media") > 7:
    print("aprovado")
else:
    print("reprovado")