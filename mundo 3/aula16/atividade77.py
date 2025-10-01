
palavras = ("aprender","comer","estuda","youx","guanabara")
for j in palavras:
    print(f"na palavra {j} temos ") 
    for letra in j:
        if letra.lower() in "aeiou":
            print(letra) 