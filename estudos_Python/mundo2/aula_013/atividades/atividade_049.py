'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o 
usuário escolher, só que agora utilizando um laço for.
'''

#Resposta

soma = 0 
numero_que_deseja_ser_cauculado = int(input('Digite o número que deseja multiplicar: '))

for c in range(0 , 10):
    soma = c + 1 
    calculo = (soma * numero_que_deseja_ser_cauculado)
    print(f'{soma} * {numero_que_deseja_ser_cauculado} = {calculo}')