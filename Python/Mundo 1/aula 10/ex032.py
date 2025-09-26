ano = int(input('Que ano você quer ver: '))
if (ano % 4 == 0):
    print(f"O ano {ano} é BISSEXTO.")
else:
    print(f"O ano {ano} não é BISSEXTO.")