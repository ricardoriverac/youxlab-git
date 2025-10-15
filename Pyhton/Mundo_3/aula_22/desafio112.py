def leiaDinheiro(msg):
    while True:
        numero1 = str(input(msg)).replace(",", ".").strip()
        cont = 0
        for c in numero1:
            if c.isalpha() == True:
                cont += 1
        if cont > 0 or n1 == "":    
            print(f"Erro! {numero1} é um preço invalido")
        else:
            break
    return float(numero1)