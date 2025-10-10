galera = list()
dados = list()
total_maior = total_menor = 0

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    dados.append(dados[:])
    dados.clear

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade ')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade ')
        total_menor += 1

print(f'Tem {total_maior} maiores de idade e {total_menor} menores de idade ')




#galera = [['joão', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos de idade')







    #teste = list()
    #teste.append('Gustavo')
    #teste.append(40)
    #galera = list()
    #galera.append(teste[:])
    #teste[0] = 'Maria'
    #teste[1] = 22
    #galera.append(teste[:])
    #print(galera)