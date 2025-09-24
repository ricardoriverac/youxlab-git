sidade = 0
sexov = 0
none = ''
idadehm = 0
mcmv = 0
for id in range (0, 4):
    nome = str(input('Qual seu nome? '))
    idade = int(input('Em qual sua idade? '))                         
    sexo = str(input('Qual seu sexo? M/F: '))
    sidade = sidade + idade
    if id == 1 and sexo == 'M' or sexo == 'm':
        sexov = sexo
    if sexo == 'M' or sexo == 'm' and idade > idadehm :
        idadehm = idade 
        none = nome
    if sexo == 'F' or sexo == 'f' and idade < 20:
        mcmv = mcmv + 1
media = sidade / 4
print ('A media de idade é {},o nome do homem mais velho é {} que tem {} anos de idade, ' \
'e existem {} mulheres com menos de 20 anos nesse grupo ' .format(media, none, idadehm, mcmv))