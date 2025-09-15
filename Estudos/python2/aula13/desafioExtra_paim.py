alunos= int(input('Quantos alunos presentes na sala de aula? ').replace('alunos', ''))
nota=0
media=0
soma=0
alunosAcima=0
b = 0
for c in range (1, alunos+1):
    soma=soma+1
    nota= int(input('Qual a nota do aluno {} ? '.format(soma)))
    
   
    media=media+nota
    if c == 1:
        notaMaior= nota
        notaMenor= nota
        
    else:
        if nota > notaMaior:
            notaMaior = nota
        if  nota < notaMenor:
            notaMenor = nota
mediaFinal=media/alunos

    
        

print(f'A menor nota da turma é {notaMenor}')
print(f'A maior nota da sala é {notaMaior}')
soma2= 0
for b in range (1, alunos+1):
    soma2=soma2+1
    nota= int(input('Redigite a nota do aluno {} para calcularmos a media ? '.format(soma2)))
    
    if nota > mediaFinal:
        alunosAcima += 1

print(f'A média de notas da turma é {mediaFinal}')
print(f'A quantidade de alunos acima da media são {alunosAcima}')