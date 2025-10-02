lista_boa = []
for c in range(0,5):
    numero = int(input("digite um numero: "))
    if c == 0:
        lista_boa.append(numero)
    elif numero > lista_boa[len(lista_boa)-1]:
        lista_boa.append(numero)   
    else: 
        pos = 0 
        while pos < len(lista_boa):
            if numero <= lista_boa[pos]:     
                lista_boa.insert(pos,numero)
                break
            pos += 1
print(f"a ordem dos valores e {lista_boa}")              