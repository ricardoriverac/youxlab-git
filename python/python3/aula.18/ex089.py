ficha = []
boletim = []
media = []
continuar = 'S'
while continuar == 'S':
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segundo nota: '))
    m = (nota1 + nota2)/2
    ficha.append(nome)
    media.append(m)
    ficha.append(media[:])
    ficha.append(nota1)
    ficha.append(nota2)
    boletim.append(ficha[:])
    media.clear()
    ficha.clear()
    continuar = str(input('Deseja continuar [S/N]?')).upper()
print(boletim)
print(f'{nome} media {media}')
print('-='*15)
for p, v in enumerate(boletim):    
    print(f"{p:<4}{v[0]:<10}{v[1][0]:>8.1f}")
print('-='*15)

