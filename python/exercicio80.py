listaUsuario = []
for c in range(5):
    numero = int(input(f'digite um valor: '))
    if c == 0:
        listaUsuario.append(numero)
    else:
        for i in range(len(listaUsuario)):
            if numero < listaUsuario[i]:
                listaUsuario.insert(i, numero)
                break
            else:
                if i == len(listaUsuario)-1:
                    listaUsuario.append(numero)
print(listaUsuario)
