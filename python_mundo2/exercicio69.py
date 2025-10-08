pcm18 = 0                                                               #pessoas com mais de 18
hc = 0                                                                  #homens cadastrados
mcm20 = 0                                                               #mulheres com menos de 20
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('qual seu sexo? [M/F]: ')).upper()
    continuar = str(input('Você deseja continuar? [S/N]: ')).upper()
    if idade < 20 and sexo == 'F':
        mcm20 = mcm20 + 1
    if idade >= 18:
        pcm18 = pcm18 + 1
    if sexo == 'M':
        hc = hc + 1
    if continuar == 'N':
        break 
    else:
        pass
print ('existem {} pessoas com mais de 18 anos no grupo, e {} homens foram cadastrados,' \
'e existem {} mulheres com menos de 20 anos  ' .format(pcm18, hc, mcm20))