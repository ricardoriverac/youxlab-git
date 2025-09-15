tamanho1 = float(input('Digite um número: '))
tamanho2 = float(input('Digite um segundo número: '))
tamanho3 = float(input('Digite um terceiro numero: '))
soma1 = tamanho1 + tamanho2
soma2 = tamanho1 + tamanho3
soma3 = tamanho2 + tamanho3
if tamanho1 < soma3 and tamanho2 < soma2 and tamanho3 < soma1:
    print('É possível fazer um triangulo com essas medidas!!')
else:
    print('não é possível fazer um triangulo com essas medidas')