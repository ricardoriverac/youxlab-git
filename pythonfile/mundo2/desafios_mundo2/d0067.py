
numero = 0
while True:
    numero = int(input('Qual tabuada você quer ver?: '))
    if numero < 0 :
        break
    print(f'''A tabuada de {numero} é 
{numero*1}
{numero*2}
{numero*3}    
{numero*4}
{numero*5}
{numero*6}
{numero*7}
{numero*8}
{numero*9}
{numero*10}''')
print('Fim do programa')