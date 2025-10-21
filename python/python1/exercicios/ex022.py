nome = str(input('Digite seu nome: '))
mai = nome.upper ()
min = nome.lower ()
esp = (nome.count (' '))
com = (len(nome) - nome.count(' ')) 
td = com - esp
sep = nome.split ()
pri = sep [0]
con = len(pri)
print(f""" Seu nome é :{nome}
    -Todo em maiusculo :{mai}
    -Todo em minusculo :{min}
    -possui {td} letras; e
    -A primeira palavra possui {com}, letras""")