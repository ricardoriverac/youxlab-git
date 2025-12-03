def ficha(nome="Fernando", gols=2):
    if not isinstance(gols, int):
        gols = 2

    print(f"Nome do jogador: {nome}")
    print(f"Gols que ele marcou: {gols}")


ficha("Roberto", 20)
print(" " )
ficha("Lucca")
print(" ")
ficha(gols=30)
print(" ")
ficha(gols="Trinta")
print(" ")
ficha()
