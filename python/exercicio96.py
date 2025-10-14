def area(largura, comprimento): #define e calcula a area
    area = largura * comprimento #multiplica a largura e o comprimento
    print(f'a area de um terreno {largura}x{comprimento} e de {area}m².')#mostrar o resultado

print('controle de terreno')
l = float(input('largura (m): '))
c = float(input('comprimento (m): '))
area(l, c)#passando os valores digitados