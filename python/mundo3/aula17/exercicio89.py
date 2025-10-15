estudantes=[]
alunos=[]
medias=[]
soma=[]
numero=0
resposta = 'S'
while resposta != 'N':
    nome=str(input('Nome: '))
    nota1=int(input('Nota 1: '))
    nota2=int(input('Nota 2: '))
    alunos.append(nome)
    medias.append(nota1)
    medias.append(nota2)
    soma=nota1+nota2
    media=soma/len(medias)
    medias.clear()
    medias.append(media)
    estudantes.append(alunos)
    estudantes.append(medias)
    alunos.clear
    medias.clear
    #estudantes.copy()
    resposta=str(input('Quer continuar? S/N ')).upper() 
    
    print(estudantes)
    print(media)