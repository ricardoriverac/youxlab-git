medida = float(input('Uma distância em metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}km, {:.0f}hm , {:.0f}dam , {:.0f}dm , {:.0f}cm , {:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))