teste=list()
teste.append('Gustavo')
teste.append(40)
galera=list()
galera.append(teste[:])
teste[0]= 'Maria'
teste[1]= 30
galera.append(teste[:])
print(galera)

galera= [['Lucas', 25], ['Pedro', 15], ['Rodrigo', 12]]
print(galera)
print(galera[0])
print(galera[1][0])
for pessoa in galera:
    print(pessoa)
    print(pessoa[0])