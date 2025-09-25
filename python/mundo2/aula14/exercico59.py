print('[1] soma ')
print('[2] multiplica ')
print('[3] maior ')
print('[4] novos numeros ')
print('[5] sair do programa ')
valor1=int(input('Digite um valor: '))
valor2=int(input('Digite outro: '))
numero=int(input('Digite a opção: '))
while numero!=5:
    if numero == 1:
        print(f'A soma deu {valor1+valor2}')
    elif numero==2:
        print(f'A multiplicação deu {valor1*valor2}')
    elif numero==3:
        if valor1>valor2:
            print(f'O maior numero é {valor1}')
    elif numero ==3:
        print(f'O maior numero é {valor2}')
    elif numero>5 or numero<1:
        print('Invalido.Tente novamente')
    elif numero==4:
        valor1=int(input('Digite um valor: '))
        valor2=int(input('Digite outro: '))
    # numero=int(input('Digite a opção: '))
print('Obrigado,volte sempre!')
