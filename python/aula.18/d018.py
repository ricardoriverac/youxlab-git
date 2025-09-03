import math
an = float(input('Digite o angulo que voce deseja:'))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('com base no valor do seu angulo,aqui esta seu seno {:.2f},cosseno {:.2f} e tangente : {:.2f}' .format(seno,cos,tan))

