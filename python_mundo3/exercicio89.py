lista = list()
mediatemp = []
mediaperm = []
nv = 0
nv2 = 0
 
nv = int(input('Quantos alunos você deseja registrar? '))
while nv2 != nv :
    nome = str(input('Qual seu nome? '))
    nota1 = float(input('Digite sua nota:'))
    nota2 = float(input('Digite sua segunda nota:'))
    mediatemp.append(nota1)
    mediatemp.append(nota2)
    media2 = mediatemp[0] + mediatemp[1]
    resultadom = media2 / 2
    lista.append([nome, resultadom])
    mediatemp.clear()
    nv2 += 1

print ('-='* 30)
print (f'{"no":<4}{"Nome":<7}{"Media":<8}')
print ('_' * 30)
for i,l in enumerate(lista):
    print(f'{i:<4}{l[0]:<7}{l[1]:<8}')