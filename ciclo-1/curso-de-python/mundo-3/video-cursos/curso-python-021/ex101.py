def voto(ano):
    idadeUsuario = 2025 - ano
    if idadeUsuario < 16:
        print(f'Sua idade é {idadeUsuario} anos, seu voto NÃO é válido.')

    elif idadeUsuario == 16 or idadeUsuario < 18 or idadeUsuario >= 65:
        print(f'Sua idade é {idadeUsuario} anos, seu voto é OPICIONAL.')

    elif idadeUsuario >= 18:
        print(f'Sua idade é {idadeUsuario} anos, seu voto é OBRIGATÓRIO.')

#Código Principal
anoUsuario = int(input('Digite seu ano de nascimento: '))
voto(anoUsuario)