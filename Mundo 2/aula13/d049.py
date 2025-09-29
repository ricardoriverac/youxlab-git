multiplo = int(input('Escolha um número para obter sua tabuada: '))
for numero in range(0,11):
    tabuada = multiplo * numero
    print(f'{multiplo} x {numero} = {tabuada}')