medida = float(input('Digite uma distancia em metros :'))
cm = medida * 100
mm = medida *1000
dec = medida * 10
km = medida / 1000
hc = medida / 100
dam = medida / 10
print('A medida de {} corresponde a {} cm\n {}mm\n {}dec\n{}km\n{}hc\n{}dam\n' .format(medida,cm,mm,dec,km,hc,dam))