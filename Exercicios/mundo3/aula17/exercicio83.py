expressao = str(input("Escreva uma expressão utilizando parenteses: "))

if expressao.startswith("(") and expressao.endswith(")"):
    print("A expressão começa e termina com parênteses.")
else:
    print("A expressão não começa e termina com parênteses.")

