primSegmento = float(input('Digite o primeiro segmento: '))
segSegmento = float(input('Digite o segundo segmento: '))
terSegmento = float(input('Digite o terceiro segmento: '))
if primSegmento < segSegmento + terSegmento and segSegmento < primSegmento + terSegmento and terSegmento < segSegmento + primSegmento:
    print('Forma um triângulo', end=' ')
    if primSegmento == segSegmento == terSegmento:
        print('EQUILÁTERO')
    elif primSegmento != segSegmento != terSegmento != primSegmento:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else: 
    print('Não forma um triângulo')