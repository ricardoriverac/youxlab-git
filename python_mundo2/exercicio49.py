nume = int(input('Qual o número você deseja obter a tabuada? '))               #numero escolhido para a tabuada
for tab in range (0, 10+1):                                                      #tabuada do numero
    print ('{} X {} = {}' .format (nume, tab, nume*tab))
