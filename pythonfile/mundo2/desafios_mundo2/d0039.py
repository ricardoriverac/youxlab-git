nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota + nota2) /2
print('A media do aluno é '.format(nota, nota2 , media))
if media >=5 and media <7:  
    print('Voce esta de recuperação')
elif media <5:
    print('Voce esta reprovado')
else:
    print('Voce esta aprovado')