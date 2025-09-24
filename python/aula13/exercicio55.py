major = 0
minor = 0 
for c in range(1, 6):
    peso = float(input(f'Qual o peso do usuário{c}? '))
    if c == 1:
        major =  peso
        minor = peso
    else:
        if peso > major:
            major = peso
        if peso < minor:
            minor = peso
print(f'O major peso lido foi de {major}Kg')
print(f'O menor peso lido foi de {minor}Kg')

'''o major e o minor são definidos incialmente como valores nulos
após definir o for e o input, são iniciados os if's
o primeiro if diz que caso o primeiro termo seja 1, os objetos major e minor são definidos como peso
isso faz com que todos os valores definidos em peso serão direcionados, também para major e minor
mas, caso o valor seja diferente de 1, ou seja, sejam direcionados mais usuários com diferentes pesos no objeto c
serão criados mais dois if's, sendo eles:
 if 1 -> ele define que caso o peso > major, significa que major = peso
ou seja, como todos os valores foram tomados como peso, o valor que for maior em peso será definido como o MAJOR
if 2 -> ele define que caso o peso < minor, ele será tomado como MINOR
mesmo caso do if anterior
depois, a informação é imprimida no terminal'''
