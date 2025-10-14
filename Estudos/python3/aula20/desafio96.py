def area(largura, comprimento):
        terreno= largura*comprimento
        print(f'A area de um terreno {largura}x{comprimento} é de {terreno} ')



largura= float(input('Qual a largura do seu terreno retangular?'))
comprimento=float(input('Qual o comprimento do seu terreno retangular? ').replace('m', ''))
area(largura, comprimento)