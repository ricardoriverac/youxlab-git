medida = float(input('Uma distancia em metros'))
cm = medida *100
mm = medida *1000
print('\033[1;30;47m A medida de {}m corresponde a {}cm e {}mm .\033[1;30;47m'.format(medida, cm, mm))