ptdc = conta = 0                                                                            #preço total da compra
qpcm = 0                                                             #quantos produtos custam mais de 1000
pmb = ''                                                                               #produto mais barato
pdmb = 0
while True :
    ndp = str(input('Qual o nome do produto? '))                                    #nome do produto 
    pdp = float(input('Qual o preço do produto? '))                                   #preço do produto
    pdmb = pdp
    conta = conta + 1
    if conta == 1:
        pdmb = pdp 
        pmb = ndp
    if pdmb < pdp :
        pmb = ndp
    ptdc = ptdc + pdp
    if pdp >= 1000:
        qpcm = qpcm + 1
    continuar = str(input('Você desja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
    else:
        pass
print ('o preço total da compra é {}R$, você comprou {} produtos com o valor acima de 1000R$' \
'e o produto mais barato é {}' .format(ptdc, qpcm, pmb))