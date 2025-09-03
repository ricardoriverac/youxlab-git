medida = float(input('Digite uma distância: '))
dam = medida / 10
hm = medida / 100
km = medida / 1000
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A média de {} corresponde {} cm\n {}mm\n {}dec\n{}km\n{}hc\n{}dam\n'.format(medida,dam,hm,km,dm,cm,mm))