t = ''
j = 0
maior = 0 
menor = 9999999999999999999999999999999999
numerodev = 0
while t != 'NÃO' :
    p = int(input('Digite um número: '))
    j = j + p
    numerodev = numerodev + 1
    g = str(input('Você deseja continuar?[SIM/NÃO]')).upper()
    t = g
    if p > maior :
        maior = p
    else:
        pass
    if p < menor:
        menor = p
media = j / numerodev 
print ('a media de todos os números é {}, o maior número é {} e o menor é {}' .format (media, maior,  menor))